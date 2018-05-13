import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)

leftAnkle = GPIO.PWM(03, 50)
rightAnkle = GPIO.PWM(03, 50)
leftKnee = GPIO.PWM(03, 50)
rightKnee = GPIO.PWM(03, 50)
leftHip = GPIO.PWM(03, 50)
rightHip = GPIO.PWM(03, 50)
leftBody = GPIO.PWM(03, 50)
rightBody = GPIO.PWM(03, 50)


def SetLeftAnkleAngle(startAngle, stopAngle):
    leftAnkle.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    leftAnkle.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    leftAnkle.ChangeDutyCycle(0)
    leftAnkle.stop()

def SetRightAnkleAngle(startAngle, stopAngle):
    rightAnkle.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    rightAnkle.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    rightAnkle.ChangeDutyCycle(0)
    rightAnkle.stop()

def SetLeftKneeAngle(startAngle, stopAngle):
    leftKnee.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    leftKnee.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    leftKnee.ChangeDutyCycle(0)
    leftKnee.stop()

def SetRightKneeAngle(startAngle, stopAngle):
    rightKnee.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    rightKnee.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    rightKnee.ChangeDutyCycle(0)
    rightKnee.stop()

def SetLeftHipAngle(startAngle, stopAngle):
    leftHip.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    leftHip.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    leftHip.ChangeDutyCycle(0)
    leftHip.stop()

def SetRightHipAngle(startAngle, stopAngle):
    rightHip.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    rightHip.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    rightHip.ChangeDutyCycle(0)
    rightHip.stop()

def SetLeftBodyAngle(startAngle, stopAngle):
    leftBody.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    leftBody.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    leftBody.ChangeDutyCycle(0)
    leftBody.stop()

def SetRightBodyAngle(startAngle, stopAngle):
    rightBody.start(startAngle)
    duty = stopAngle / 18 + 2
    GPIO.output(03, True)
    rightBody.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    rightBody.ChangeDutyCycle(0)
    rightBody.stop()

def LeftLeg(oldAnkle, oldKnee, oldHip, oldBody, newAnkle, newKnee, newHip, newBody):
    SetLeftAnkleAngle(oldAnkle, newAnkle)
    SetLeftKneeAngle(oldKnee, newKnee)
    SetLeftHipAngle(oldHip, newHip)
    SetLeftBodyAngle(oldBody, newBody)

def RightLeg(oldAnkle, oldKnee, oldHip, oldBody, newAnkle, newKnee, newHip, newBody):
    SetRightAnkleAngle(oldAnkle, newAnkle)
    SetRightKneeAngle(oldKnee, newKnee)
    SetRightHipAngle(oldHip, newHip)
    SetRightBodyAngle(oldBody, newBody)

GPIO.cleanup()
