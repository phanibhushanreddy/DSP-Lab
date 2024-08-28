def cyclic_delay(x,m):
    N=len(x)
    y=[]
    for n in range(0,N):
        if(n-m>=0):
            index=(n-m)%N
        else:
            index=N+n-m
        y.append(x[index])
    return y
x=[1,2,3,4,5]
m=1
result=cyclic_delay(x,m)
print(result)