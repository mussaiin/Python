import random
import time
comp = 0
user = 0
computer = 0
tr1 = 0
tr2 = 0
tr0 = bool(True)
while True:
    print("Rock...")
    time.sleep(0.1)
    print("Paper...")
    time.sleep(0.1)
    print("Scissors...")
    print("Choose (rock = 1 / scissors = 2 / paper = 3)")
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
        print("                                                              YOU won with ", tr1," tries")
        print("Again? y - yes/n - no")
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
        print("                                                               COMPUTER won with ", tr2," tries")
        print("Again? y - yes/n - no")
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
