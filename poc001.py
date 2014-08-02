
#!/usr/bin/python
import time
import RPi.GPIO as GPIO

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

#GPIO 12 100Hz
p = GPIO.PWM(12, 100)

p.start(100)

time.sleep(1)



p.ChangeDutyCycle(50)
time.sleep(1)

p.ChangeDutyCycle(25)
time.sleep(1)

p.sttop()


