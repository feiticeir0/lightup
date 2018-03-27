from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

#pin connected to relay
relay_pin = 23
#pin state
pin = 1

GPIO.setmode (GPIO.BCM)
GPIO.setup (relay_pin, GPIO.OUT)

#default route, without anything
@app.route("/")
def default():
	# read pin state
	pin = GPIO.input(relay_pin)
	return render_template ('lights.html',pin=pin)


# set a route for action
# light on or off
@app.route("/<status>")
def onAction(status):
	pin = 2
	if status == "on":
		pin = 0
		GPIO.output (relay_pin, GPIO.LOW)
		#message =  "Light on!"
		print ("on")
	if status == "off":
		pin = 1
		GPIO.output (relay_pin, GPIO.HIGH)
		#message = "Light off!"
		print ("off")
	
	# return to the template with new info
	return render_template ('lights.html',pin=pin)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)


