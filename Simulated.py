import random
import math

def getProb(dE,T):
    return math.exp(-(dE))/T

def getFunct(x1,x2):
    return (-(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-(math.sqrt((x1**2)+(x2**2))/math.pi))))))

def getNewRandInRange(x):
    newX = x + random.uniform(-1, 1)
    while (newX > 10) or (newX < -10):
        newX = x + random.uniform(-1, 1)
    return newX

x1,x2 = random.uniform(-10,10),random.uniform(-10,10)
current = getFunct(x1,x2)
best = current

T = 1000000         #Suhu awal
Tmin = 0.00001      #Suhu minimum
a = 0.9999          #Cooling rate

while (T>Tmin):
    y1,y2 = getNewRandInRange(x1),getNewRandInRange(x2)
    new = getFunct(y1,y2)
    dE = new - current
    if (new<current):
        current = new
        x1=y1
        x2=y2
        best = current
    elif (getProb(dE,T)>random.random()):
        x1=y1
        x2=y2
        new = current
    T *= a
print('best solusion = ',best)
