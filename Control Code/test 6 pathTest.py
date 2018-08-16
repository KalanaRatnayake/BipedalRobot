from invKinematics import invKinematic
import numpy as np

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
    q2 = 0.8

    qpath = []
    
    for i in range(0, len(pathArray)):
        x = round(pathArray[i].item(0),3)
        y = round(pathArray[i].item(1),3)
        z = round(pathArray[i].item(2),3)

        q1,q2 = invKinematic(x, y, z, q1, q2)
        
        qpath.append([convertToDegree(q1), convertToDegree(q2)])
    else:
        return qpath

routePointArray = np.matrix([[-0.03, 0.25, 0], [0, 0.21, 0], [0.01, 0.21, 0], [0.03, 0.25, 0], [-0.03, 0.25, 0]])
timeGapArray = np.matrix([[1.5], [1.5], [1.5], [5.5]])

path = producePath(routePointArray,timeGapArray, 0.5)

qpath = produceAngles(path)

for i in range(len(qpath)):
    print qpath[i]
