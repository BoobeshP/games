import numpy as np

def fun(a1,x,min,max):
    mid = (min + max)//2
    if x[mid] == a1:
        print("Number is found & index is ", mid)
    elif x[mid] > a1:
        max = mid
        fun(a1,x,min,max)
    else:
        min = mid
        fun(a1, x, min, max)

x =[]
for i in range(50):
    a1 = np.random.randint(0,2000)
    x.append(a1)
    x.sort()

print(x,"\n"*3)
a1 = int(input("Enter a number in list : "))
if a1 not in x:
    print("Enter number in list only work here")
else:
    a2 = fun(a1,x,min = 0,max = len(x)-1)