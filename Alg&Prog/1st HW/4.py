n=int(input("Enter N: "))
a=[]
median=0
for i in range(1,n+1):
    m=float(input("Enter %s number: " %i))
    a.append(m)
    median = (sum(a))/n
print("Maximum is: ", max(a))
print("Minimum is: ", min(a))
print("Median is: ", median)
