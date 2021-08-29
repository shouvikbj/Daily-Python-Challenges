# have to write this python code without using any "/" or "%" operator

numOfHotDogs = 400
numOfHotDogInOnePacket = 8
requiredPackages = 0

tempCount = 0

for i in range(1, numOfHotDogs + 1):
    tempCount += 1
    if tempCount == 8:
        requiredPackages += 1
        tempCount = 0

print(requiredPackages)
