import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

leftAnkle = GPIO.PWM(37, 50)
rightAnkle = GPIO.PWM(40, 50)
leftKnee = GPIO.PWM(35, 50)
rightKnee = GPIO.PWM(38, 50)
leftHip = GPIO.PWM(33, 50)
rightHip = GPIO.PWM(36, 50)
leftBody = GPIO.PWM(31, 50)
rightBody = GPIO.PWM(32, 50)


def SetLeftAnkleAngle(angle):
    leftAnkle.start(0)
    duty = angle / 18 + 2
    GPIO.output(37, True)
    leftAnkle.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(37, False)
    leftAnkle.ChangeDutyCycle(0)
    leftAnkle.stop()

def SetRightAnkleAngle(angle):
    rightAnkle.start(0)
    duty = angle / 18 + 2
    GPIO.output(40, True)
    rightAnkle.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(40, False)
    rightAnkle.ChangeDutyCycle(0)
    rightAnkle.stop()

def SetLeftKneeAngle(angle):
    leftKnee.start(0)
    duty = angle / 18 + 2
    GPIO.output(35, True)
    leftKnee.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(35, False)
    leftKnee.ChangeDutyCycle(0)
    leftKnee.stop()

def SetRightKneeAngle(angle):
    rightKnee.start(0)
    duty = angle / 18 + 2
    GPIO.output(38, True)
    rightKnee.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(38, False)
    rightKnee.ChangeDutyCycle(0)
    rightKnee.stop()

def SetLeftHipAngle(angle):
    leftHip.start(0)
    duty = angle / 18 + 2
    GPIO.output(33, True)
    leftHip.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(33, False)
    leftHip.ChangeDutyCycle(0)
    leftHip.stop()

def SetRightHipAngle(angle):
    rightHip.start(0)
    duty = angle / 18 + 2
    GPIO.output(36, True)
    rightHip.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(36, False)
    rightHip.ChangeDutyCycle(0)
    rightHip.stop()

def SetLeftBodyAngle(angle):
    leftBody.start(0)
    duty = angle / 18 + 2
    GPIO.output(31, True)
    leftBody.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(31, False)
    leftBody.ChangeDutyCycle(0)
    leftBody.stop()

def SetRightBodyAngle(angle):
    rightBody.start(0)
    duty = angle / 18 + 2
    GPIO.output(32, True)
    rightBody.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(32, False)
    rightBody.ChangeDutyCycle(0)
    rightBody.stop()

def LeftLeg(newAnkle, newKnee, newHip, newBody):
    SetLeftAnkleAngle(newAnkle)
    SetLeftKneeAngle(newKnee)
    SetLeftHipAngle(newHip)
    SetLeftBodyAngle(newBody)

def RightLeg(newAnkle, newKnee, newHip, newBody):
    SetRightAnkleAngle(newAnkle)
    SetRightKneeAngle(newKnee)
    SetRightHipAngle(newHip)
    SetRightBodyAngle(newBody)


LeftLeg(30,20,80,0)
sleep(1)
LeftLeg(30,110,80,0)

GPIO.cleanup()
