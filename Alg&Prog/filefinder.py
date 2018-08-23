import os
import string
def copy():
    fin = open('text.txt', 'r')
    fout = open('text1.txt', 'w')
    for line in fin:
        fout.write(line)
    fout.close()

def charcount():
    fin = open('text.txt', 'r')
    fout = open('text1.txt', 'w')
    for line in fin:
        line = line.strip('\n')
        fout.write(line+' '+str(len(line))+'\n')
    fout.close()
 
def file(name):
    if(os.path.isfile(name)):
        print("It is a file and it is placed in", os.path.abspath(name))
    elif(os.path.isdir(name)):
        print("It is a directory and has these files in it: ", os.listdir(name))
    elif not(os.path.exists(name)):
        print("Doesn't exist.")

