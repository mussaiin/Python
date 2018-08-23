print("Enter triangle's parameters")
x1=int(input("X1: "))
y1=int(input("Y1: "))
x2=int(input("X2: "))
y2=int(input("Y2: "))
x3=int(input("X3: "))
y3=int(input("Y3: "))
print("Enter point coordinates")
x0=int(input('X: '))
y0=int(input('Y: '))

a=(x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
b=(x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
c=(x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)

if(a==b or a==c):
    print('inside')
elif(a==0 or b==0 or c==0):
    print('on the circle')
else:
    print('outside')
