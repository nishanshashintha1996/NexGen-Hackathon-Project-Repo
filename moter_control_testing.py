import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)

    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.005)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.006)
    GPIO.cleanup()






