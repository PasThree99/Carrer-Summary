from scipy.stats import chi2
from math import ceil



def getNumberOfIntervals(n):
    op =[6,10,5,2,3,4,7,8,9]
    op.extend([i for i in range(10,100)])
    numOfInt = 0
    for i in op:
        if n%i == 0:
            numOfInt = i
            break
    
    return numOfInt


def sigueDistrUniforme(numbers:list) ->bool:
    n = len(numbers)
    numOfInt = getNumberOfIntervals(n)
    cv = 1/numOfInt
    intervals = [cv*i for i in range(0,numOfInt+1)]
    couter = [0 for i in range(numOfInt)]
    for i in range(1,len(intervals)):
        for j in numbers:
            if(j < intervals[i] and j > intervals[i-1]):
                couter[i-1] += 1 
    
    expected = [n/numOfInt for i in range(len(couter))]

    s = []

    for i in range(len(expected)):
        s.append(((couter[i]-expected[i]) **2)/expected[i])
    
    X = chi2.isf(0.05,numOfInt-1)
    if(sum(s) < X):
        return True
    else:
        return False

    
    
def congruencialMultiplicativo(seed:int, mod:int, a:int, n:int):
    semilla = seed
    modelo=lambda x: a*x

    num_act=0
    num_obt=semilla


    k=0
    #print(k,semilla)


    num_max=n
    lf = []
    flag = False

    while(k<num_max):
        if(num_act == semilla):
            flag = True
        num_act=num_obt
        num_obt=modelo(num_act) % mod
        #print(k+1,num_obt/mod)
        lf.append(num_obt/mod)
        num_act=num_obt
        k+=1
    return (lf, sigueDistrUniforme(lf))

    


def cuadradosDeEnmedio(seed:int, n:int):
    c = 0
    lf = []
    while(c < n):
        cuadado = seed**2
        st = str(cuadado)
        ex = ""

        #st = "1651225"

        if(len(st)%2 == 0):
            l = len(st)
            l = l-4
            l = int(l/2)
            ex = st[l:l+4]
        else:
            l = len(st)
            l = l-4
            l = l/2
            l = ceil(l)
            ex = st[l-1:l+3]

        newNum = int(ex)
        seed = newNum
        while(newNum > 1):
            newNum = newNum/10
        lf.append(newNum)


        c += 1
        
    return (lf,sigueDistrUniforme(lf))




