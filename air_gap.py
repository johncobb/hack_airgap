#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

# Configuration
FAN_PIN = 24            # BCM pin used to drive transistor's base
LED_PIN = 18
WAIT_TIME = 5           # [s] Time to wait between each refresh
SPOOL_TIME = 2          # [s] Time to wait for fan to spool down
FAN_MIN = 20            # [%] Fan minimum speed.
PWM_FREQ = 25           # [Hz] Change this value if fan has strange behavior

# Configurable temperature and fan speed steps
tempSteps = [50, 70]    # [°C]
speedSteps = [0, 100]   # [%]

dotSleep = 1
dashSleep = 2

puaseSleep = 2


# Fan speed will change only of the difference of temperature is higher than hysteresis
hyst = 1

# Setup GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

fan=GPIO.PWM(FAN_PIN,PWM_FREQ)

fan.start(0)


i = 0
cpuTempOld=0
fanSpeed = 0
fanSpeedOld=0


CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

print "running air_gap hack..."

try:
    while (1):

        msg = 'HELLO WORLD'


        for char in msg:
            if char == ' ':
                print ''
                continue

            for code in CODE[char.upper()]:
                if code == '.':
                    print 'dot'
                    GPIO.output(LED_PIN, 1)
                    fan.ChangeDutyCycle(40)
                    time.sleep(dotSleep)
                    fan.ChangeDutyCycle(0)
                    GPIO.output(LED_PIN, 0)
                    time.sleep(SPOOL_TIME)
                    
                elif code == '-':
                    print 'dash'
                    GPIO.output(LED_PIN, 1)
                    fan.ChangeDutyCycle(50)
                    time.sleep(dashSleep)
                    fan.ChangeDutyCycle(0)
                    GPIO.output(LED_PIN, 0)
                    time.sleep(SPOOL_TIME)
                else:
                    print ''
            
        print 'pause...'
        time.sleep(5)
            

# If a keyboard interrupt occurs (ctrl + c), the GPIO is set to 0 and the program exits.
except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()


