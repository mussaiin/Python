t=[1,2,3]
t2=[5,7]
t3=[10,0]
t2.extend(t3)
t.append(t2)
print(t)

def f(d):
    t=dict()
    for k in d:
        v = d[k]
        if v not in t:
            t[v] = k
        else:
            t[v].append(k)
    return t

   
print(f({1:2, 1:3, 2:3}))
#            k:v,  k:v,  k:v 
