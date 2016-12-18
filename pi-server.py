from sense_hat import SenseHat
import web
import json
import io
import time
import picamera

sense = SenseHat()
sense.low_light = True

urls = (
	'/', 'index',
	'/temperature', 'temp',
	'/humidity', 'humidity',
    '/pressure', 'index',
    '/orientation', 'index',
	'/show', 'show',
	'/camera', 'camera'
)

class index:
    def GET(self):
        return "Raspeberry Pi"

class temp:
	def GET(self):
		result = { 'temperature': sense.get_temperature_from_pressure() }
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header( 'Content-Type', 'application/json' )
		return json.dumps( result )

class humidity:
	def GET(self):
		result = { 'humidity': sense.humidity }
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header( 'Content-Type', 'application/json' )
		return json.dumps( result )

class show:
	def POST(self):
		data = web.input()
		scrollspeed = 0.1
		if 'speed' in data :
			scrollspeed = float(data.speed)
		sense.show_message(data.message, scrollspeed)

#class camera:
#	def GET(self):
		#my_stream = io.BytesIO()
		#with picamera.PiCamera() as camera:
		#camera.start_preview()
		# Camera warm-up time
		#time.sleep(2)
		#camera.capture(my_stream, 'jpeg')
		#camera.stop_preview()
		#web.header('Access-Control-Allow-Origin', '*')
		#web.header('Access-Control-Allow-Credentials', 'true')
		#web.header( 'Content-Type', 'images/jpeg' )
		#return json.dumps( result )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
