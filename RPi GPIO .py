#physcal 11
#BCM 17
# led resistor 300

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
    GPIO.output(11,1)
    print ("ok on")
    sleep(2)
    GPIO.output(11,0)
    print ("ok offf")
    sleep(2)
    



