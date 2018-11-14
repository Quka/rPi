from sense_hat import SenseHat
import socket

sense = SenseHat()

# Setup UDP socket for broadcasting
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)

server.bind(("", 44444))

while(True):
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # The message to send
    msg = "C = %s, P = %s H = %s" % (t, p, h)
    # Encode the message to bytes and in utf-8 (default)
    msgBytes = msg.encode()

    # Broadcast message to port 37020 via UDP Socket
    server.sendto(msgBytes, ('<broadcast>', 37020))

    sense.show_message( "sent", scroll_speed=0.05 )