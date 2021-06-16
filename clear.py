# GPIO traffic light program
# pin numbers
GPIO_RED = 22
GPIO_AMBER = 23
GPIO_GREEN = 24
GPIO_SWITCH = 17
# time delay in secs
TIME = 1
# import RPi.GPIO module
import RPi.GPIO as GPIO
# import time module used for sleep
import time
# Use GPIO pin numbering disable in-use warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Setup relevant pins
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_AMBER, GPIO.OUT)
GPIO.setup(GPIO_GREEN, GPIO.OUT)
GPIO.setup(GPIO_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# start with red light on
GPIO.output(GPIO_RED, False)
GPIO.output(GPIO_AMBER, False)
GPIO.output(GPIO_GREEN, False)
