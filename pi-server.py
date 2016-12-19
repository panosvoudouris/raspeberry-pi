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
	'/matrix', 'matrix',
	'/camera', 'camera'
)

class index:
    def GET(self):
        return "Raspeberry Pi"

class temp:
	def GET(self):
		result = { 'data': sense.get_temperature_from_pressure() }
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header( 'Content-Type', 'application/json' )
		return json.dumps( result )

class humidity:
	def GET(self):
		result = { 'data': sense.humidity }
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header( 'Content-Type', 'application/json' )
		return json.dumps( result )

class show:
	def POST(self):
		data = json.loads(web.data())
		print data
		scrollspeed = 0.1
		if 'speed' in data :
			scrollspeed = float(data['speed'])
		sense.show_message(data['message'], scrollspeed)

class matrix:
	def POST(self):
		data = json.loads(web.data())
		print data
		sense.set_pixels(data['matrix'])


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
