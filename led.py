#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

led_on = False
count = 0


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def flashLED(count):
    for i in range(count):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(18, GPIO.LOW)
        time.sleep(.2)


def switch(ev=None):
    global led_on, count
    led_on = not led_on
    count += 1

    if led_on == True:
        print("Turning on\tcount: " + str(count))
        GPIO.output(18, GPIO.HIGH)
    else:
        print("Turning off\tcount: " + str(count))
        GPIO.output(18, GPIO.LOW)


def detectButtonPress():
    GPIO.add_event_detect(23, GPIO.FALLING, callback=switch, bouncetime=300)


def waitForEvents():
    while True:
        time.sleep(1)


# # # # # MAIN # # # # #

def main():
    print("# # # LED Program # # #")
    print("LED:\tpin 18")
    print("Button:\tpin 23")

    setupGPIO()
    flashLED(5)
    detectButtonPress()

    waitForEvents()


if __name__ == "__main__":
    main()
