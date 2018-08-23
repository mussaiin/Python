"""
zhansaya@amanatlabs.com
1)def fact
2)1000-sum
print(sum(3)) 1000 - 3
print(sum(3,32)) 1000 - 35 
print(sum(3,32,43)) 1000 - 78

n = int(input())
if(n%2==0):
    if(n%4==0):
        print("Yes")
    else:
        print("E")
else:
    print("Y")
"""
"""
n=int(input())
sum = 0
for i in range(1, n+1):
    sum=sum+i
print(sum)

def abc(a,b,c):
    ans = 0
    ans = a*b//c
    print(ans)
abc(2,3,1)
abc(4,5,2)
abc(4,5,2)

def hello():
    print("Hello, World!")
hello()

def s(x):
    return x*5
y=s(5)+5
print(y)

def getGender(g='unknown'):
    if g == 'm':
        g='Male'
    elif g == 'f':
        g = 'Female'
    print(g)

getGender('m')
getGender('f')
getGender()

def wthr(w="I don't know"):
    if w == 's':
        w='snow'
    elif w == 'r':
        w = 'rain'
    elif w == 'z':
        w='sun'
    return w
print(wthr('s'))
print(wthr('r'))
print(wthr('z'))
print(wthr())

a=[1,2,3,4,5]
def sum(s):
    ans = 0
    for i in range(a[0,3]):
        ans=ans+i
    return ans
y=sum(ans)
print(y)


a=[1,2,3,4,5]
def sum():
    ans = a[0]+a[1]+a[2]
    return ans
y=sum()
print(y)


a=[1,2,3,4,5]
def sum(*arg):
    total=0
    for i in arg:
        total = total+i
    return total
print(sum(3))
print(sum(3,32))
print(sum(3,32,43))

zhansaya@amanatlabs.com
1)def fact
2)1000-sum
print(sum(3)) 1000 - 3
print(sum(3,32)) 1000 - 35 
print(sum(3,32,43)) 1000 - 78

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans=ans*i
    print(ans)
m=int(input())
fact(m)

def sum(*arg): # * когда массив
    total=0
    num = 1000
    for i in arg:
        total = total+i
    return num - total
print(sum(3))
print(sum(3,32))
print(sum(3,32,43))

def sum(*arg): # * когда массив
    total=0
    for i in arg:
        total = total + i
        if total % 2 == 0:
            return True
        elif total % 2 == 1:
            return False
print(sum(2))
print(sum(3,3))
print(sum(3,32,43))

def health(age, apples, cig):
    ans=(100-age)*(apples*3.5)-(cig-2)
    print(ans)

health(17,2,1)
h=[18,3,0]
health(h[0],h[1],h[2])
health(*h)

def sent(name = 'Zhansaya ',action = 'sits'):
    print(name+action)
sent()
sent('Vlad ', 'runs')

def qwe(name='Nurlybek ', age='17'):
    print(name + age)

h=['Aziz ', '18']
q=['Qwe ', '15']
qwe()
qwe(*h)
qwe(*q)

classmates={'Zhansaya':1, 'Sana':2, 'Aziz':3, 'Nurlybek':4, 'Sherkhan':5} #called dictionary
print(classmates)
for v,k in classmates.items(): # .items() для dictionary
    if (k%2==0):
        print(v)
        
n=int(input())
for i in range(6):
    if(n==i):
        break
"""
"""
import random

while True:
    number = random.randint(1,10)
    tr = 5
    print("Ugaday chislo ot 1 do 10")
    while True:
        if(tr==0):
            print("Game Over!")
            print("Eshe? y - yes/n - no")
            ans=str(input())
            if(ans=='y'):
                tr=5
            elif(ans=='n'):
               break
        print("U tebya", tr," popytok")
        guess=int(input())
        if(number<guess):
            print('menshe')
            tr = tr-1
        if(number==guess):
            print('You win!')
            break
        if(number>guess):
            print('bolshe')
            tr = tr-1
"""
import random
import time
comp = 0
user = 0
computer = 0
tr1 = 0
tr2 = 0
tr0 = bool(True)
while True:
    print("Су...")
    time.sleep(0.1)
    print("Ли...")
    time.sleep(0.1)
    print("Фа...")
    print("введите свой выбор(камень=1/ножницы=2/бумага=3)")
    player = input()
    #player.lower()
    while(player!='1' and player!='2' and player!='3'):
        print(player)
        player=input("введите еще раз")
    comp=random.randint(1,3)
    if(comp == 1): comp = '1'
    if(comp == 2): comp = '2'
    if(comp == 3): comp = '3'
    if(comp == player):
        print("Ничья")
        tr1 = tr1+1
        tr2 = tr2+1
        continue
    if(player=='1'):
        if(comp =='2'):
            print("You win!")
            user = user+1
            tr1 = tr1+1
            tr2 = tr2+1
        else:
            print("You lose!")
            computer = computer+1
            tr1 = tr1+1
            tr2 = tr2+1
    if(player=='2'):
        if(comp == '3'):
            print("You win!")
            user = user+1
            tr1 = tr1+1
            tr2 = tr2+1
        else:
            print("You lose!")
            computer = computer+1
            tr1 = tr1+1
            tr2 = tr2+1
    if(player=='3'):
        if(comp == '1'):
            print("You win!")
            user = user+1
            tr1 = tr1+1
            tr2 = tr2+1
        else:
            print("You lose!")
            computer = computer+1
            tr1 = tr1+1
            tr2 = tr2+1
    if(computer<user and user==3):
        print("You won with ", tr1," tries")
        print("Eshe? y - yes/n - no")
        ans=str(input())
        if(ans=='y'):
            tr1=0
            tr2=0
            computer=0
            user=0
            continue
        elif(ans=='n'):
            #break
            tr0 = False
    elif(computer>user and computer==3):
        print("Computer won with ", tr2," tries")
        print("Eshe? y - yes/n - no")
        ans=str(input())
        if(ans=='y'):
            tr1=0
            tr2=0
            computer=0
            user=0
            continue
        elif(ans=='n'):
            #break
            tr0 = False
    if(tr0==False):
        break
