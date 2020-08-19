import random

listLength = 100

inputNum = open("sortInput.txt", "w")

for i in range(listLength) :
    inputNum.write(str(random.randint(1, 1000))+"\n")


inputNum.close()



numbers = open('sortInput.txt', 'r')
outputNum = open ("sortOutput.txt", "w")

numList = []

def bubbleSort(list):
    for i in range(len(list)):
        count = 0
        while count < len(list) - i - 1 :
            if(list[count] > list[count + 1]) :
                temp  = list[count]
                list[count] = list[count + 1]
                list[count + 1] = temp
            count += 1
    return list


for num in numbers:
    numList.append(int(num) )

for num in bubbleSort(numList) :
    outputNum.write(str(num) + "\n")
