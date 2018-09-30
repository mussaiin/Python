f1=open("input.txt", "r")
tm=f1.readline()
intm=int(tm)
for i in range(intm):
    line=f1.readline()
    a=line.split()
    
#ans=int(line)+int(line2)
f2=open("output.txt", "w")
f2.write(str(a))
f1.close()
f2.close()
"""
#1 2
f=open("input.txt", "r")
line=f.read(1)
line2=f.read(3)
ans=int(line)+int(line2)
f=open("output.txt", "w")
f.write(str(ans))
f.close()
"""
"""
#1
#2
f=open("input.txt", "r")
line=f.readline()
line2=f.readline()
ans=int(line)+int(line2)
f=open("output.txt", "w")
f.write(str(ans))
f.close()
"""
"""
f=open("input.txt", "w")
f.write("hello students")
f.close()
"""
"""
f=open("input.txt", "r")
line=f.readline() #readline() считывает строку 
print(line)
f.write("hello students")
f.close()
"""
"""
a=int(input())
b=int(input())
c=a+b
f=open("output.txt", "w")
f.write(str(c))
f.close()
"""

