import random
minLen=3 #variabile di stop per la ricorsione


def sampleMedianSelect(list,k):
    #k posizione dell'elemento da ritornare
    if k < 0 or k > len(list):
        return None
    return recursiveSelect(list, 0, len(list)-1, k,minLen)

def recursiveSelect(l, left, right, k,minLen): #verificare cos'è minLen

    long=(right-left)+1
    m=int(long*0.5) #parametro che specifica la grandezza di V


    if long<=minLen:

        item=trivialSelect(l[left: right + 1], k - left)
        return item

    V = randomChoice(l[left:right+1],m)  # V pari ad una lista di len = m di elementi random di list

    piv=sampleMedianSelect(V,int(m/2))
    perno=partitionDet(l,left,right,piv)

    #condizioni di ricerca
    posperno = perno + 1

    if posperno == k:

        return l[perno]
    if posperno > k:

        return recursiveSelect(l, left, perno - 1, k, minLen)
    else:

        return recursiveSelect(l, perno + 1, right, k, minLen)

#funzione che crea il sotto insieme V
#tale funzione crea una lista casuale di dimensione dim prelevando elementi da list
def randomChoice(list, dim):

    limit = len(list)

    if limit<dim:
        return list
    new = random.sample(list,dim)
    return new

#funzione usata per partizionare
def partitionDet(l, left, right, pivot):
    #nota: pivot è un valore dell'array l e non un indice!
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    return sup

def trivialSelect(l, k):

    length = len(l)
    if length < 0:
        return None

    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]

    return l[k - 1]

if __name__ == '__main__':

    random.seed(160)
    l = [None]*20
    for i in range(0, 20):
        l[i] = random.randint(-100,100)
    print(l)
    print(len(l))
    a=sampleMedianSelect(l,5)#il valore di k deve essere compreso tra 1 e len
    print(a)
    print(l)
