import numpy as np
def cyclic_delay(x,m):
    N=len(x)
    return [x[(n-m)%N] for n in range(N)]
def circ_conv(x1,x2):
    N=len(x1)
    M=len(x2)
    x2_padded=x2+[0] * (N - M)
    z=[]
    for n in range(N):
        y=cyclic_delay(x2_padded,n)
        z.append(np.dot(x1,y))
    return z
x1=[1,2,3,4]
x2=[-1,0,5,3]
result=circ_conv(x1,x2)
print(result)