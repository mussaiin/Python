import os, pickle, dbm

def database1():
    db=dbm.open('file.db', 'c')
    
    s='string'
    d={'key':'val'}
    file=open('a.txt', 'r')
    f=file.read()

    db['1']=pickle.dumps(s)
    db['2']=pickle.dumps(d)
    db['3']=pickle.dumps(f)

    for k in db:
        print(pickle.loads(db[k]))
    db.close()
    
def findtxt(way):
    txt=[]
    for root, dirs, files in os.walk(way):
        for file in files:
            if(file[-4:]=='.txt'):
                 txt.append(file)
    for i in txt:
        print(i)
        
