n=int(input())
#x=[]
x=''
x=str(x)
while(n!=0):
    ans=int(n%2)
    #x.append(ans)
    x=x+str(ans)
    n=int(n/2)
#x.reverse()
    
print(x[::-1])

