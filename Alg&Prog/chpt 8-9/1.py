'''
word=input()
for i in range(len(word)):
    print(word[-i-1],end='')
'''
'''
def wrd(word, letter):
    count=1
    for i in range(len(word)):
        if(word[i]==letter):
            print(i)
            break
        elif(word[i]!=letter):
            count=count+1
        if(count==len(word)-1):
            print('-1')     
'''
'''
def wrd(word, letter):
    count=0
    for i in range(len(word)):
        if(word[i]==letter):
            count=count+1
    return count
'''
'''
def wrd(word):
    a=[]
    b=[]
    for i in range(len(word)//2):
        a.append(word[i])
        word=word[::-1]
    for j in range(len(word)//2):
        b.append(word[j])
    if(a==b):
        print("True")
    else:
        print("False")
'''
'''
def wrd(word, index):
    if(index==0):
        new_word=''+word[index+1:]
    else:
        new_word=word[:index]+''+word[index+1:]
    return new_word
'''
'''
def wrd(word):
    first=word[0]
    last=word[len(word)-1]
    new_word=last+''+word[1:(len(word))-1]+''+first
    return new_word
'''
'''
def wrd(word, n):
    new_word=''
    for i in word:
        new_word=new_word+chr(ord(i)+n)
    return new_word
'''
'''9.6
def wrd(word):
    word1=sorted(word)
    word2=[]
    for i in word:
        word2.append(i)
    if word2 == word1:
        return True
    else:
        return False
'''
