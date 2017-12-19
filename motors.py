# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 29,31,33,35,37,40

RightMotor = 29
RM1a = 31
RM1b = 33

LeftMotor = 40
LM1a = 35
LM1b = 37

sleeptime=1

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RightMotor, GPIO.OUT)
    GPIO.setup(LeftMotor, GPIO.OUT)

    GPIO.setup(RM1a, GPIO.OUT)
    GPIO.setup(RM1b, GPIO.OUT)
    GPIO.setup(LM1a, GPIO.OUT)
    GPIO.setup(LM1b, GPIO.OUT)


def forward(x):
    #H-Bridge Pin Settings
    GPIO.output(RM1a, GPIO.HIGH)
    GPIO.output(RM1b, GPIO.LOW)
    GPIO.output(LM1a, GPIO.HIGH)
    GPIO.output(LM1b, GPIO.LOW)

    #Turning Motors ON
    GPIO.output(RightMotor, GPIO.HIGH)
    GPIO.output(LeftMotor, GPIO.HIGH)
    print ("Moving Forward")
    time.sleep(x)
    GPIO.output(RightMotor, GPIO.LOW)
    GPIO.output(LeftMotor, GPIO.LOW)

def reverse(x):
    #H-Bridge Pin Settings
    GPIO.output(RM1a, GPIO.LOW)
    GPIO.output(RM1b, GPIO.HIGH)
    GPIO.output(LM1a, GPIO.LOW)
    GPIO.output(LM1b, GPIO.HIGH)

    #Turning Motors On
    GPIO.output(RightMotor, GPIO.HIGH)
    GPIO.output(LeftMotor, GPIO.HIGH)

    print ("backwarding running motor")
    time.sleep(x)

    GPIO.output(RightMotor, GPIO.LOW)
    GPIO.output(LeftMotor, GPIO.LOW)


def dance(x):
    #H-Bridge Pin Settings
    GPIO.output(RM1a, GPIO.LOW)
    GPIO.output(RM1b, GPIO.HIGH)
    GPIO.output(LM1a, GPIO.HIGH)
    GPIO.output(LM1b, GPIO.LOW)

    #Turning Motors On
    GPIO.output(RightMotor, GPIO.HIGH)
    GPIO.output(LeftMotor, GPIO.HIGH)

    print ("Dancing!")
    time.sleep(x)

    GPIO.output(RightMotor, GPIO.LOW)
    GPIO.output(LeftMotor, GPIO.LOW)

def destroy():
    print ("Stopping motor")
    GPIO.cleanup()


if __name__ == '__main__':     # Program start from here
  setup()
  try:
    reverse(5)
  except :  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()

  time.sleep(1)
  try:
      forward(5)
  except:
      destroy()

  #time.sleep(1)
  #try:
  #    dance(5)
  #except:
  #    destroy()

  destroy()
