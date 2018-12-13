
from MedianSelect import *


def Sort(list):  # funzione di ordinmento della lista (il nome è fittizio)
    Mod_Quick_Sort(list, 0, len(list) - 1)  #chimata al modify quickSort

def Mod_Quick_Sort(list,left,right):
    #la scelta del pivot e' lasciata alla funzione sampleMedianSelect
    long = right - left
    new = list[left:right+1]
    if left >= right:
        return

    pivot = sampleMedianSelect(new,int(long/2)) #forse mettere long/2

    mid = partitionDet(list, left, right, pivot)#funzione inclusa in median select
    Mod_Quick_Sort(list,left,mid - 1)
    Mod_Quick_Sort(list,mid + 1,right)



if __name__ == '__main__':
    #Breve esempio di funzionamento
    l=[None]*100
    for i in range(0,100):
        l[i]=random.randint(-100,100)

    #l=[]
    #l = [3,4,7,2,2,2,2,2,2,24,4,4,4,4,4,6,7,5,4,2,2,53,4232,2423,6455,-39,-123,-98,4,6, 14, 5, 6, 3, 2, 0]
    print(l)
    Sort(l)
    print(l)



