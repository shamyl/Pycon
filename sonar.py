#Sonar interface with the Raspberry PI

#Import Python libraries
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 29    #GPIO_24
GPIO_ECHO = 40        #GPIO_25

#Set Pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN) # Echo

#Set Trigger low
GPIO.output(GPIO_TRIGGER, False)

#Allow module to settle
time.sleep(0.5)

def sonar():
    #Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    #Calculate pulse length
    elapsed = stop-start

    #Distance pulse traveled in that time is time
    #multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    #That was the total distance so half it for reaching the object
    distance = distance /2

    return distance

while True:
    time.sleep(0.3)

    distance = sonar()
    print (distance)
