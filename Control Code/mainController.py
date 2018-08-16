from invKinematics import invKinematic
import numpy as np
import smbus
import math
import RPi.GPIO as GPIO
from time import sleep


#####------------settting up servo setup for legs----------------#####
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

leftAnkle = GPIO.PWM(37, 50)    #left Ankle on pin 37
rightAnkle = GPIO.PWM(40, 50)   #right Ankle on pin 40
leftKnee = GPIO.PWM(35, 50)     #left knee on pin 35
rightKnee = GPIO.PWM(38, 50)    #right knee on pin 38
leftHip = GPIO.PWM(33, 50)      #left hip on pin 33
rightHip = GPIO.PWM(36, 50)     #right hip on pin 36

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

#####------------Methods to control each joint servo-------------#####
def SetLeftAnkleAngle(angle):
    leftAnkle.start(0)
    duty = angle / 18 + 2
    GPIO.output(37, True)
    leftAnkle.ChangeDutyCycle(duty)
    sleep(1)
    #leftAnkle.stop()

def SetRightAnkleAngle(angle):
    rightAnkle.start(0)
    duty = angle / 18 + 2
    GPIO.output(40, True)
    rightAnkle.ChangeDutyCycle(duty)
    sleep(1)
    #rightAnkle.stop()

def SetLeftKneeAngle(angle):
    leftKnee.start(0)
    duty = angle / 18 + 2
    GPIO.output(35, True)
    leftKnee.ChangeDutyCycle(duty)
    sleep(1)
    #leftKnee.stop()

def SetRightKneeAngle(angle):
    rightKnee.start(0)
    duty = angle / 18 + 2
    GPIO.output(38, True)
    rightKnee.ChangeDutyCycle(duty)
    sleep(1)
    #rightKnee.stop()

def SetLeftHipAngle(angle):
    leftHip.start(0)
    duty = angle / 18 + 2
    GPIO.output(33, True)
    leftHip.ChangeDutyCycle(duty)
    sleep(1)
    #leftHip.stop()

def SetRightHipAngle(angle):
    rightHip.start(0)
    duty = angle / 18 + 2
    GPIO.output(36, True)
    rightHip.ChangeDutyCycle(duty)
    sleep(1)
    #rightHip.stop()


#####---------methods to control a whole leg at once----------#####
def LeftLeg(newAnkle, newKnee, newHip):
    SetLeftAnkleAngle(180-newAnkle)
    SetLeftKneeAngle(90-newKnee)
    SetLeftHipAngle(180-newHip)

def RightLeg(newAnkle, newKnee, newHip):
    SetRightAnkleAngle(newAnkle)
    SetRightKneeAngle(90+newKnee)
    SetRightHipAngle(newHip)



#####---------Method to read values form gyroscope------------#####
def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def leftFoot_Y_Angle():
    bus.write_byte_data(0x68, power_mgmt_1, 0)
    return read_word_2c(0x45) #returns the angle of rotation around y axiss of ankle

def rightFoot_Y_Angle():
    bus.write_byte_data(0x69, power_mgmt_1, 0)
    return read_word_2c(0x45) #returns the angle of rotation around y axiss of ankle


#####---------------Methods to control robot along path--------------#####
def convertToDegree(rad):
    return int((rad/3.14)*180)

def producePath(routePointsArray, timeGapArray, unit):
    path =[]
    
    for j in range(0, len(timeGapArray)):
        lineVector = routePointsArray[j+1]-routePointsArray[j]
        count = int(timeGapArray[j].item(0)/unit)
        unitVector = lineVector/count
        
        for i in range(0,count):
            path.append(routePointArray[j]+(unitVector*i))
    else:
        return path

def produceAngles(pathArray):
    q1 = 1
    q2 = 1

    qpath = []
    
    for i in range(0, len(pathArray)):
        x = round(pathArray[i].item(2),3)
        y = round(pathArray[i].item(1),3)
        z = round(pathArray[i].item(0),3)

        q1,q2 = invKinematic(x, y, z, q1, q2)
        
        qpath.append([convertToDegree(q1), convertToDegree(q2)])
    else:
        return qpath

def walk(qpath):
    leftPose = 0
        
    while(True):
        rightPose = (leftPose + 50)%100

        #leftFoot = leftFoot_Y_Angle()
        #rightFoot = rightFoot_Y_Angle()

        LeftLeg(0, qpath[leftPose][1], qpath[leftPose][0])
        RightLeg(0, qpath[rightPose][1], qpath[rightPose][0])

        leftPose += 1
        leftPose %= 100

    

routePointArray = np.matrix([[0.25, 0, -0.05], [0.21, 0, 0], [0.21, 0, 0.01], [0.25, 0, 0.05], [0.25, 0, -0.05]])
timeGapArray = np.matrix([[1.5], [1.5], [1.5], [5.5]])

path = producePath(routePointArray,timeGapArray, 0.1)
qpath = produceAngles(path)

walk(qpath)

GPIO.cleanup()
