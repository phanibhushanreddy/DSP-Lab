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
x=[]
n=int(input("How many numbers do you want to enter: "))
for i in range(0,n):
    t=int(input("Enter values: "))
    x.append(t)
m=int(input("Enter the delay: "))
result=cyclic_delay(x,m)
print(result) 
