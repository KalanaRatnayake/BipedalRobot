from invKinematics import invKinematic
import numpy as np
import serial
import smbus
import math
import RPi.GPIO as GPIO
from time import sleep

arduino = serial.Serial('/dev/ttyACM0',9600)

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

def sendToArduino(q1,q2,q3,q4,q5,q6):
    string = ''
    
    sq1 = str(q1)
    sq2 = str(q2)
    sq3 = str(q3)
    sq4 = str(q4)
    sq5 = str(q5)
    sq6 = str(q6)

    if (len(sq1)==1):
        sq1 = "00"+sq1
    elif (len(sq1)==2):
        sq1 = "0"+sq1

    if (len(sq2)==1):
        sq2 = "00"+sq2
    elif (len(sq2)==2):
        sq2 = "0"+sq2

    if (len(sq3)==1):
        sq3 = "00"+sq3
    elif (len(sq3)==2):
        sq3 = "0"+sq3

    if (len(sq4)==1):
        sq4 = "00"+sq4
    elif (len(sq4)==2):
        sq4 = "0"+sq4

    if (len(sq5)==1):
        sq5 = "00"+sq5
    elif (len(sq5)==2):
        sq5 = "0"+sq5

    if (len(sq6)==1):
        sq6 = "00"+sq6
    elif (len(sq6)==2):
        sq6 = "0"+sq6

    string = sq1 + sq2 + sq3 + sq4 + sq5 + sq6 + "x"

    arduino.write(string)

def walk(qpath):
    leftPose = 0
        
    while(True):
        rightPose = (leftPose + len(qpath)/2)%len(qpath)

        sendToArduino(0, qpath[leftPose][1], qpath[leftPose][0], 0, qpath[rightPose][1], qpath[rightPose][0])

        leftPose += 1
        leftPose %= 100


routePointArray = np.matrix([[0.25, 0, -0.05], [0.21, 0, 0], [0.21, 0, 0.01], [0.25, 0, 0.05], [0.25, 0, -0.05]])
timeGapArray = np.matrix([[1.5], [1.5], [1.5], [5.5]])

path = producePath(routePointArray,timeGapArray, 0.1)
qpath = produceAngles(path)

walk(qpath)

GPIO.cleanup()
