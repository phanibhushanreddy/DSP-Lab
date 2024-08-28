import numpy as np
def cyclic_delay(x,m):
    N=len(x)
    return [x[(n-m)%N] for n in range(N)]
def circ_conv(x1,x2):
    N=len(x1)
    M=len(x2) 
    x2_padded=x2+[0]*(N-M) 
    z=[]
    for n in range(N):
        y=cyclic_delay(x2_padded,n)
        z.append(np.dot(x1,y))
    return z
def get_input_list(prompt):
    while True:
        try:
            user_input = input(prompt)
            input_list = list(map(int, user_input.split()))
            return input_list
        except ValueError:
            print("Invalid input. Please enter a list of integers separated by spaces.")
x1 = get_input_list("Enter the first list (x1) of integers separated by spaces: ")
x2 = get_input_list("Enter the second list (x2) of integers separated by spaces: ")
result = circ_conv(x1, x2)
print("Circular convolution result:", result)
