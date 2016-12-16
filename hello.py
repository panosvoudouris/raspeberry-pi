from sense_hat import SenseHat

sense = SenseHat()
sense.show_message("PIZZA", 0.1)

temp = sense.get_temperature()
#print("Temperature: %s C" % temp)

north = sense.get_compass()
print("North: %s" % north)
