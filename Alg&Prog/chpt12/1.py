n=('a',2,[1])
a=(1,2,'a',3,1,'b','a')
def ex1(n):
    a,b,c=n[0],n[1],n[2]
    print(a,b,c)
def ex2(n):
    s=''
    for i in n:
        s=s+str(i)
    print(s)
def ex3(t):
    b=dict()
    for i in t:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    return b
def ex4(t, n):
    a=()
    a=a+t[:n]+t[(n+1):]
    return a
def ex5(a,b):
    d=dict()
    c=0
    for i in a:
        d[i]=b[c]
        c+=1
    return d
