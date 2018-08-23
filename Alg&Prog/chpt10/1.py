t = ['b','a']
'''
def nested_sum(n):
    sm=0
    sm1=0
    for i in n:
        if(type(i)==list):
            for j in i:
                sm=sm+j        
        else:
            sm=sm+i;
    return sm
'''
'''
def cumsum(t):
    s=[]
    sm=0
    for i in range(len(t)):
        if(i==0):
            s.append(t[0])
        else:
            t[i]=t[i]+t[i-1]
            s.append(t[i])
    return s
'''
'''
def is_sorted(t):
    s=sorted(t)
    if(t==s):
        return True
    else: return False
'''
'''
def is_anagram(a, b):
    a=sorted(a)
    b=sorted(b)
    if(a==b):
        return True
    else:
        return False
'''
'''
def readwords():
    fin=open('words.txt')
    for line in fin:
            for word in line.split():
                s=[]
                s.append(word)
                print(s)
'''
