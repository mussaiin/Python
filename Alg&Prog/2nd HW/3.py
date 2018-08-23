'''
n=float(input("$:"))
while(n>=0):
    print(2, end='$ ')
    n=n-2
if(n>=2):
    print(1, end=' ')
    n=n-1;
if(n>=0):
    print("0.25$", end=' ')
    
'''
n=10/3
print(round(n, 2))
