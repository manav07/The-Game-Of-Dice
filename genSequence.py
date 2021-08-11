import random

def genSequence(n):
    a=[i for i in range(1,n+1)]
    sequence=[]
    for i in range(n-1,0,-1):
        tmp=random.randint(1,i)
        sequence.append(a[tmp])
        del a[tmp]
    sequence.append(a[0])
    return sequence