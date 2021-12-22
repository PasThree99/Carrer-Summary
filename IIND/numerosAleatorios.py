import matplotlib.pyplot as plt


def rangeNumbers(numbers:list, range:tuple) -> list:
    li = min(range[0],range[1])
    ls = max(range[0],range[1])
    r = ls - li

    if(li == ls):
        return numbers
    
    lf = []


    c = r/max(numbers)

    for i in numbers:
        lf.append(int(i*c + li))
    

    return lf
    


def cuadradosDeEnmedio(seed:int, n:int, range:tuple) -> list:
    nuevo_num=0
    num_obt=seed
    #print('0',seed)
    k=1
    num_max=n
    lf = []
    while(nuevo_num!=seed and k<=num_max):
        nuevo_num=num_obt
        cuad=nuevo_num**2
        string=str(cuad)
        if(len(string)%2!=0):
            string='0'+string
        quitar=(len(string)-4)/2
        
        i=int(quitar)
        numfin=''
        while(i<len(string)-quitar):
            numfin+=string[i]
            i+=1
        num_obt=int(numfin)
        
        dec=num_obt
        
        while(dec>1):
            dec/=10
        
        #print(k,dec)
        lf.append(dec)
        nuevo_num=num_obt
        k+=1
    return rangeNumbers(lf,range)

def frequency(l):
    arr = []
    print(max(l))
    for i in range(max(l)+1):
        arr.append(0)
    
    for i in l:
        arr[i-1] += 1
    return arr

l = cuadradosDeEnmedio( 23456, 1000, (10,20)) 
print(l)
f = frequency( l )




plt.bar(range(len(f)), f)
plt.show()