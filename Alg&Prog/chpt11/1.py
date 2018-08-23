def findval(d, v):
    for k in d:
        if d[k] == v:
             return k
def sozdik():
    a=dict()
    a['apple']='yabloko'
    a['compote']='kampot'
    a['orange']='apelsin'
    a['rule']='pravilo'
    a['hello']='privet'
    while True:
        print("1. Search \n2. Add\n3. Delete\n4. Exit")
        num=int(input("Enter a number of operation:"))
        if(num==1):
            word=input()
            if(word not in a):
                print(findval(a, word))    
            else:
                print(a.get(word))
        elif(num==2):
            word=input("Enter the word in EN:")
            word1=input("Enter the translation:")
            a[word]=word1
        elif(num==3):
            word=input("Enter the word which do you want to delete:")
            if(word not in a):
                a.pop(findval(a, word))
            else:
                a.pop(word)
        elif(num==4):
            break;
