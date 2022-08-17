import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp =='w':
        if you == 's':
            return False
        elif you=='g':
            return True


print('Comp Turn : Snake(s) Water(w) or Gun(g)')
randno=random.randint(1,2)
if randno == 1:
    comp='s'
elif randno==2:
    comp='w'
elif randno=='3':
    comp='g'

you = input('Your Turn : Snake(s) Water(w) or Gun(g)?')
a=gamewin(comp,you)
print(f'computer chose {comp}')
print(f'You Chose {you}')
if a==None:
    print("TIE!")
elif a==True:
    print("Congratulations, you win!")
elif a==False:
    print("You Lose, try again! 'good luck'")

