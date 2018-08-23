import math
import copy

class point:
    x=0
    y=0

'''
def dist(a, b):
    print(math.sqrt((b.x - a.x)**2 + (b.y-a.y)**2))

p=point()
p.x=10
p.y=10

p2=point()
p2.x=4
p2.y=3

dist(p, p2)
'''

class rect:
    p=point()
    w=0
    h=0
#r1=rect()
#print('r1: ', r1.w, r1.h, r1.p.x, r1.p.y)

def inc(r, a, b, c, d):
    r.w=r.w+a
    r.h=r.h+b
    r.p.x=r.p.x+c
    r.p.y=r.p.y+d
    return r

r=rect()
r.w=100
r.h=50
r.p.x=10
r.p.y=10
a=inc(r, 80, 30, 5, 15)
print(a.w, a.h, a.p.x, a.p.y)
r2=copy.copy(r)

'''
def find_center(r):
    p=point()
    p.x=r.w/2+r.p.x
    p.y=r.h/2+r.p.y
    return p
a=find_center(r1)
print(a.x, a.y)
'''
