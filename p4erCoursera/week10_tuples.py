#Tuples are immutable

# tuples cannot be sorted, extend etc. You can do count and index. 

# Tuples are more efficient than lists. They are temporary lists. 

(x, y) = ('4', 'fred')
x, y = ('4', 'fred')

# each thing inside a list is a tuple
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
  print k, v
  
tups = d.items()
print tups

# Tupels are comparable. If the first item is similar python goes to the second otherwise it doesn't

Things that can be compared can also be sorted.

d = {'a':10, 'b': 1, 'c':22}
t = d.items()
t
t.sort()
t

# sorted() is a parameter that takes a sequence as a aprameter and return a sorted list

d = {'a':10, 'b': 1, 'c':22}
d.items()
t = sorted(d.items())


for k,v in sorted(d.items()):
  print k,v

# we want to sort in terms of values rather than keys. We mkae a temporary list and then we append and we add values and keys.

# with a for loop construct a list of tuples and then sort the list by value

c = {'a':10, 'b': 1, 'c':22}
tmp = list()

for k,v in c.items() : 
  tmp.append( v, k )
  

print tmp
tmp.sort(reverse=True)
print tmp

# the 10 most common words.

fhand = open('romeo.txt')
counts = dict()

for line in fhand:
  words = line split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts items():
  lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst[:10]:
  print key, val
  
# shorter way to do this:
c = {'a':10, 'b': 1, 'c':22}
print sorted([(v,k) for k,v in c.items()])

# list comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.

# http://wiki.python.org/moin/HowTo/Sorting
  
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.
  
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = dict()        
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        tmp = words[5]
        hrs = tmp.split(':')
        time[hrs[0]] = time.get(hrs[0], 0) + 1

lst = list()
for key, val in time.items():
    lst.append((key, val))

lst.sort()

for val, key in lst:
    print val, key