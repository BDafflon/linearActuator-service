from rrb3 import *
from random import randint
from flask import Flask
from json import dumps
 


app = Flask(__name__)

rr = RRB3(12, 12) # Battery voltage 12V, motor 12V

T = 20  # 20 seconds to extend

extended = True
 

@app.route('/start/<delai>')
def start(delai):
    T=delai
    return "ready"
    

@app.route('/stop')
def stop():
    rr.cleanup() # Set all GPIO pins to safe input state


@app.route('/extending')
def extending():
    print("extending")
    rr.set_led2(True)
    rr.forward(T, 1.0)
    rr.set_led2(False)
    extended = True
    return True

@app.route('/retracting')
def retracting():
    print("retracting")
    rr.set_led1(True)  # LED 1 on
    rr.reverse(T, 1.0)
    rr.set_led1(False)
    extended = False
    return True

if __name__ == '__main__':
     app.run(port='5002')
