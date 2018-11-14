from sense_hat import SenseHat
import socket

sense = SenseHat()
timestamp = datetime.now

def setup_udp_socket():
    # Setup UDP socket for broadcasting
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    server.settimeout(0.2)

    server.bind(("", 44444))
    return server

def get_sense_data():
    sense_data = {
        't': round(sense.get_temperature(), 1),
        'p': round(sense.get_pressure(), 1),
        'h': round(sense.get_humidity(), 1),
        'date': datetime.now()
    }
    
    return sense_data

server = setup_udp_socket()

while(True):
    data = get_sense_data()
    time = data[-1] - timestamp # træk timestamp fra datetime i data

    if time.seconds > delay:
        # The message to send
        msg = "C = %s, P = %s H = %s" % (t, p, h)
        # Encode the message to bytes and in utf-8 (default)
        msgBytes = msg.encode()

        dataBytes = data.encode()

        # Broadcast message to port 37020 via UDP Socket
        server.sendto(dataBytes, ('<broadcast>', 37020))

        sense.show_message( "sent", scroll_speed=0.05 )