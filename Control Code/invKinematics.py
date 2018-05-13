import math
import numpy

def derivative(f1, f2, q1, q2, x, z, h):
    return numpy.matrix([[((f1(q1+h, q2 ,x) - f1(q1, q2 ,x)) / h), ((f1(q1, q2+h ,x) - f1(q1, q2 ,x)) / h)],[((f2(q1+h, q2 ,z) - f2(q1, q2 ,z)) / h) , ((f2(q1, q2+h ,z) - f2(q1, q2 ,z)) / h)]])

def eqnX(q1, q2, x):
    return 0.180*math.cos(q1+q2)+0.160*math.cos(q1)+0.035-x

def eqnZ(q1, q2, z):
    return 0.180*math.sin(q1+q2)+0.160*math.sin(q1)-z

def solve(funcX, funcZ, q1, q2, x, z, h):
    lastQ = numpy.matrix([[q1], [q2]])
    nextQ = lastQ + 10* h

    error = abs(nextQ - lastQ)
    
    while (error.item(0) > h and error.item(1)>h ):
        
        newEQN = numpy.matrix([[funcX(lastQ.item(0), lastQ.item(1), x)], [funcZ(lastQ.item(0), lastQ.item(1), z)]])
        
        deriva = derivative(funcX, funcZ, lastQ.item(0), lastQ.item(1), x, z, h)
        
        nextQ = lastQ - deriva.getI()*newEQN

        error = abs(nextQ - lastQ)

        lastQ = nextQ
    else:
        return nextQ.item(0), nextQ.item(1)

def invKinematic(x,z,q1,q2):
    newQ1, newQ2 = solve(eqnX, eqnZ, q1, q2, x, z, 0.01)
    return newQ1, newQ2
