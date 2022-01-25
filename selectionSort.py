listNum = [9,9,5,6,3,2,7,10,11,12]
maxNum = 0
windowSize = len(listNum)
while windowSize != 0:
    for i in range(windowSize):
        if listNum[i] > listNum[maxNum]:
            maxNum = i
        if i == windowSize-1:
            listNum[i], listNum[maxNum] = listNum[maxNum], listNum[i]
        else: pass
    handsOff = 0
    maxNum = 0
    windowSize -= 1
print(listNum)