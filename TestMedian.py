from MedianSelect import *
from time import time

# crea una lista
def createList(steps,type):
    random.seed(1)  #genera la stessa sequenza per generare casualità nei risultati
    inputList = [None] * steps
    inputType = type  # 1 crescente, -1 decrescente, 0 random

    for i in range(0, steps):
        if inputType == 1:
            inputList[i] = i
        elif inputType == -1:
            inputList[i] = steps - i
        elif inputType == 0:
            inputList[i] = random.randint(0, steps)
        else:
            raise Exception("You used an invalid inputType parameter!")



    return inputList

# salva dati in un file
def salvaInFile(name,long,time):

    file=open(name,'a')
    file.write("{},{}\n".format(long,time))
    file.close()

#somma elementi di una lista
def listSomma(l):
    som=0
    for i in range(0,len(l)):
        som+=l[i]
    return som

def testMedian(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        sampleMedianSelect(inputList,int(len(inputList)/2))
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long

    salvaInFile("Median_02.csv", steps, risultato)

if __name__ == '__main__':

    # Inizializzazione
    #grandezza stringa steps
    first = True
    second = True
    third = True
    fourth = False

    if first:
        for steps in range(5,501,5):
            testMedian(steps,10)

        for steps in range(1000,5001,50):
            testMedian(steps, 10)

    if second:
        for steps in range(5000,50001,500):
            testMedian(steps, 5)

    if third:

        for steps in range(100000,500001,50000):
            testMedian(steps, 2)

    if fourth:
        for steps in range(500000,1000001,200000):
            testMedian(steps, 2)
