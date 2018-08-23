mass=int(input())
cost=0
if(mass>0 and mass<=30):
    cost=40
elif(mass>30 and mass<=50):
    cost=55
elif(mass>50 and mass<=100):
    cost=70
elif(mass>100):
    if(mass<=150):
        cost=95
    elif(mass>150):
        cost=70+25*((mass-100)//50)
print("Cost is", cost, "sinas")
