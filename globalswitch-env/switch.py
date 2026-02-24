from flask import Flask, jsonify, render_template
from flask_cors import CORS
import RPi.GPIO as GPIO

app = Flask(__name__, template_folder="switch_web")
CORS(app)  # allow cross-origin requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

state = False

@app.route('/')
def index():
    return render_template('globalswitch.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    global state
    state = not state
    GPIO.output(17, state)
    return jsonify({'state': state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

