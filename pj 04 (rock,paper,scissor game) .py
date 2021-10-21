import random as x

def play():
    a=input("Enter r or p or s [rock,paper,scissor]:")
    b=x.choice(['r','p','s'])

    if a==b:
        return "Tie"
    if find(a,b):
        return "Won"
    return "Lose"
def find(a,b):
    if (a=='r'and b=='s') or (a=='p' and b=='r') or (a=='s' and b=='p'):
        return True


print(play())