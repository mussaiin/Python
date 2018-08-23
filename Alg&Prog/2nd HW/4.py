import random
n=3
while(n>=0):
    a=[random.randint(1, 15)]
    b=[random.randint(1, 50)]
    c=[random.randint(25, 50)]
    print(a,'* x +', b, '=', c, end='')
    print()
    n=float(input('Answer:'))
    ans=(c[0]-b[0])/a[0]
    ans=round(ans, 2)
    if(ans==n):
        print("correct, answer is", ans)
        n=n-1
        a=[];b=[];c=[]
    else:
        print("incorrect, answer is", ans)
        n=n-1
        a=[];b=[];c=[]
