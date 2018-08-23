import math
import copy

class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "x: %d y: %d" %(self.x, self.y)
    def __add__(self, p):
        return self.x+p.x, self.y+p.y
    def change_point(self, a, b):
        self.x+=a
        self.y+=b
        
class rect:
    p=point()
    p.x=0
    p.y=0
    w=2
    h=1

class circ:
    C=point()
    R=10

a=point(0,0)
print(a)
a.change_point(1,1)
print(a)
p=point()
p.x=1
p.y=1
c=circ()
c.C.x=0
c.C.y=0
r=rect()

def point_in_circle(cir, po):
    if(((cir.C.x-po.x)**2 + (cir.C.y-po.y)**2)<=(cir.R)**2):
        return True
    else:
        return False
        
def rect_in_circle(r, c):
    p=copy.copy(rect.p)

    if not point_in_circle(c, p):
        return False
    p.x += rect.w
    
    if not point_in_circle(c, p):
        return False
    p.y -= rect.h
    
    if not point_in_circle(c, p):
        return False
    p.x -= rect.w
    
    if not point_in_circle(c, p):
        return False
    return True 
