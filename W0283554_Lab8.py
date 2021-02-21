from guizero import *
from gpiozero import AngularServo
from time import sleep
from gpiozero import Servo

def slider_angle(slider_num):
    n = slider_num
    servo1 = AngularServo(gpio20, min_pulse_width = minPW, max_pulse_width = maxPW, initial_angle = 0)
    servo1.angle = int(n)
    print(n)
    sleep(.5)
    
def slider2_angle(slider2_num):
    n2 = slider2_num
    servo2 = AngularServo(gpio21, min_pulse_width = minPW, max_pulse_width = maxPW, initial_angle = 0)
    servo2.angle = int(n2)
    print(n2)
    sleep(.5)

app = App("RC servo controlPos", height=150)
slider1 = Slider(app, width="fill", start=(-90), end=90, command = slider_angle)
textbox = TextBox(app)
slider2 = Slider(app, width="fill", start=(-90), end=90, command = slider2_angle)
textbox = TextBox(app)

gpio20 = 20
gpio21 = 21

correct1 = .6
correct2 = 0.5
maxPW = (2.0 + correct1)/1000
minPW = (1.0 - correct2)/1000


app.display()
