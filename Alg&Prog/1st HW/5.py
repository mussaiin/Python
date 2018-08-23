x=0
for i in range(51):
    if(i%6==0):
        continue
    elif(i%2==0):
        x=x+i
        print(i)
    elif(i%3==0):
        x=x+i
        print(i)
print("Sum is: ", x)
