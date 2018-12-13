from time import time
from Modify_Quick_Sort import *
import Sorting


#calcolo del tempo di esecuzione
def timeTest(inputList, sortingFunction):
    l = list(inputList)  # copy the list Equivalent to l=input[:].
    start = time()
    sortingFunction(l)
    return time() - start

#crea una lista
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

#salva dati in un file
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

#test con elementi random modQuick
def test1(steps,number):


    timeList = []

    inputList = createList(steps, 0)
    for i in range(0,number): #range numero dei test


            runningTime = timeTest(inputList,Sort)

            timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_mod_quick_ran_05.csv",steps,risultato)

#test con elementi crescenti modQuick
def test2(steps,number):
    timeList = []

    inputList = createList(steps, 1)
    for i in range(0,number): #range numero dei test


            runningTime = timeTest(inputList,Sort)

            timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_mod_quick_cre.csv",steps,risultato)

#test con elementi decrescenti modQuick
def test3(steps,number):
    timeList = []

    inputList = createList(steps, -1)
    for i in range(0,number): #range numero dei test


            runningTime = timeTest(inputList,Sort)

            timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_mod_quick_dec.csv",steps,risultato)

#test con sort di python su lista random
def test4(steps,number):
    timeList = []
    inputList = createList(steps,0)

    for i in range(0,number):
        start = time()
        inputList.sort()
        runningTime = time()-start
        timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_python_sort.csv",steps,risultato)

#test bubbleSort
def test5(steps,number):
    timeList = []
    inputList = createList(steps,0)

    for i in range(0,number):
        start = time()
        Sorting.bubbleSort(inputList)
        runningTime = time()-start
        timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_bubble.csv",steps,risultato)

#test selectionSort
def test6(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.selectionSort(inputList)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_selection.csv",steps,risultato)

#test quickSort
def testQuick(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.quickSort(inputList)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_quickSort.csv", steps, risultato)

#test insertiondown/up
def test1Ins(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.insertionSortUp(inputList)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_Inser_up.csv", steps, risultato)

#test sul sort di python con stringa ordinata
def testOrdList(steps,number):
    timeList = []
    inputList = createList(steps,1)

    for i in range(0,number):
        start = time()
        inputList.sort()
        runningTime = time()-start
        timeList.append(runningTime)

    long=len(timeList)
    somma=listSomma(timeList)
    risultato=somma/long

    salvaInFile("test_python_sort_ordinato.csv",steps,risultato)

#test merge
def testMerge(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.mergeSort(inputList)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_merge.csv", steps, risultato)

#test heap
def testHeap(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.heapSort(inputList)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_Heap.csv", steps, risultato)

#test radix
def testRadix(steps,number):
    timeList = []
    inputList = createList(steps, 0)

    for i in range(0, number):
        start = time()
        Sorting.radixSort(inputList,steps,10)
        runningTime = time() - start
        timeList.append(runningTime)

    long = len(timeList)
    somma = listSomma(timeList)
    risultato = somma / long
    salvaInFile("test_radix.csv", steps, risultato)


if __name__ == '__main__':

    # Inizializzazione
    #grandezza stringa steps
    first = True
    second = True
    third = True
    fourth = False

    if first:
        for steps in range(5,501,5):
            test1(steps,10)
            #test2(steps,10)
            #test3(steps,10)
            #test5(steps,10)
            #testQuick(steps,5)
            #test1Ins(steps,5)
            #testOrdList(steps,5)
            #testHeap(steps, 5)
            #testRadix(steps,5)

        for steps in range(1000,5001,50):
            test1(steps,10)
            #test2(steps,10)
            #test3(steps,10)
            #test5(steps,10)
            #testQuick(steps, 5)
            #test1Ins(steps, 5)
            #testOrdList(steps, 5)
            #testHeap(steps, 5)
            #testRadix(steps, 5)

    if second:
        for steps in range(5000,50001,500):
            test1(steps,2)
            #test2(steps,2)
            #test5(steps,2)
            #testQuick(steps,2)
            #test1Ins(steps, 2)
            #testOrdList(steps, 5)
            #testHeap(steps, 5)
            #testRadix(steps, 5)

    if third:

        for steps in range(100000,500001,50000):
            test1(steps,2)
            #test2(steps,2)
            #test3(steps,2)
            #testQuick(steps,2)
            #test1Ins(steps, 2)
            #testOrdList(steps, 5)
            #testHeap(steps, 5)
            #testRadix(steps, 2)

    if fourth:
        for steps in range(500000,1000001,200000):
            test1(steps,2)
            #testQuick(steps, 2)
            #test1Ins(steps, 2)
            #testOrdList(steps, 5)
            #testHeap(steps, 5)
