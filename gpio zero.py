#physcal 11
#BCM 17


from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    print ("on")
    sleep(2)
    led.off()
    print ("off")
    sleep(2)
