# Allow to put differnt values - associative arrays. 

# The key is the label and the value is whatever

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse

print purse['candy']

print purse {'money': 12, 'tissue':75, 'candy': 3}

purse['candy'] = purse['candy'] + 2

# order is not preserved in dictionaries
# key and values

# dictionaries literals. They are some kind of data structure. 

ccc['csev'] = 1
# check if the value is there
if 'csev' in cc

vounts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names:
  if name not in counts:
    counts[name] = 1
  else
    counts[name] = counts[name] + 1
print counts    

# GET

print counts.get(name, 0) # default value if the key does not exists

counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names:
  counts[name] = counts.get(name, 0) + 1
print counts    
# in this case the code other create or update

# counting pattern
counts = dict()
print 'enter a line of text:'
line = raw_input('')

words = line.split()
print 'Words:', words

print 'Counting...'
for word in words:
  counts[word] = counts.get(word,0) + 1
  
print 'Counts', counts

# definite loops and dictionaries

for key in counts:
  print key, counts[key]
  
# retrieving lists of Keys and Values  
print list(jjj)
print jjj.keys()
print jjj.values()


# two iterations variables
jjj = {'chuck':1, 'fred':42, 'jan':100}
for aaa,bbb in jjj.items():
  print aaa, bbb
  
# the first variable is the key (aaa), and the second the value (bbb)

name = raw_input("Enter file:")
handle = open(name, 'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
  counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for word,count in counts.items():
  if bigCount is None or count > bigCount:
    bigWord = word
    bigCount = count

print bigWord, bigCount


#assignment
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

persons = dict()        
for line in handle:
    line = line.rstrip()
    if line.startswith('From: '):
        words = line.split()
        persons[words[1]] = persons.get(words[1], 0) + 1

#print persons

bigCount = None
bigWord = None
for word,count in persons.items():
  if bigCount is None or count > bigCount:
    bigWord = word
    bigCount = count

print bigWord, bigCount

### first attempts

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = text.split()

persons = dict()
for word in words:
  counts[word] = counts.get(word, 0) + 1
    
bigCount = None
bigWord = None
for word,count in counts.items():
  if bigCount is None or count > bigCount:
    bigWord = word
    bigCount = count

print bigWord, bigCount
