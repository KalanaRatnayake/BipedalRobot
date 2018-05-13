from invKinematics import invKinematic

def convertToDegree(rad):
    return int((rad/3.14)*180)

inputFile = open("test_input.txt")
outputFile = open("test_output.txt")

sampleInput = []
sampleOutput = []
 
for line in inputFile:
    words = line.split()

    sampleInput.append([float(words[0]), float(words[2])])

for line in outputFile:
    words = line.split()

    sampleOutput.append([float(words[1]), float(words[2])])

q1 = -0.5
q2 = 0.8
    
for i in range(0,100):
    x = sampleInput[i][0]
    z = sampleInput[i][1]
    
    q1, q2 = invKinematic(x, z, q1, q2)

    print "expected = ", convertToDegree(sampleOutput[i][0]), convertToDegree(sampleOutput[i][1]), "          got = ", convertToDegree(q1), convertToDegree(q2)

    

