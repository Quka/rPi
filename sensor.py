from sense_hat import SenseHat

sense = SenseHat()


while(True):
  tc = sense.get_temperature()
  tch = sense.get_temperature_from_humidity()
  
  tc = round(tc, 1)
  tch = round(tch, 1)
  
  msg = "TempC = %s, TempHumC = %s" % (tc, tch)
  
  sense.show_message( msg, scroll_speed=0.1 )