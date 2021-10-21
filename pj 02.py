import random as r

def guess(x):
    random=r.randint(1,x)
    while True:
       g=int(input("Number:"))
       if g==random:
           print("Correct answer")
           break
       elif g>random:
           print("U choose greater number")
       else:
           print("U choose lower number")

x=int(input("Enter range:"))
guess(x)