import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('text.txt')

def most_common(hist):
    t=[]
    
    for key, value in hist.items():
        if(len(key)>=5): #not articles
            t.append((value, key))
    t.sort(reverse=True)
    return t
t = most_common(hist)
print('The most common words are:')
for freq, word in t[:10]:
    print(word, freq, sep='\t')


############################################
def wordcount():
    fin = open("text.txt")
    count=0
    for words in fin.read().split():
        words = words.strip(string.punctuation + string.whitespace)
        words = words.lower()
        count+=1
    return count

def eachword(word):
    fin = open("text.txt")
    count=0
    for words in fin.read().split():
        words = words.strip(string.punctuation + string.whitespace)
        words = words.lower()
        if(word==words):
            count+=1
    print(count)
