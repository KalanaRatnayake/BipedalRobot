import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)

leftAnkle = GPIO.PWM(03, 50)

def SetAngle(startAngle, stopAngle):
    pwm.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()

GPIO.cleanup()
