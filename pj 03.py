import random as r

def guess(x):
    low=1
    high=x
    while True:
       if low==high:
           print(low)
           break
       g=r.randint(low,high)      #same high and low shows error
       print(g)
       f=input("[c or high or low]  :")
       if f=='c':
           print("Correct answer")
           break
       elif f=='high':
           print("U choose greater number")
           high=g-1
       elif f=='low':
           print("U choose lower number")
           low=g+1
       else:
           print("Wrong input")

x=int(input("Enter range:"))
guess(x)