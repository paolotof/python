list1 = ['name1', 'name2', 'name3']

for friend in list1:
  print friend
  
# friend[0] is the first  
# lists are mutable whereas string are not mutable/immutable
len(list1)
# lists can have different types in it

list1 = [1, 2, 3, 4, 'hello', 5]
range(4)

# range shows the indexes of the list
for i range(len(friends)):
  friend = friends[i]
  print 'happy new year, ', friend
  
# lists can be concatenated with '+'
# lists can be sliced as well
lists[1:4]
lists[:4]
lists[4:]
#  check out the list methods. 
stuff = list() # starts an empty list
stuff.append('book')
stuff,append(99)

# is something in a list?
some = [1, 2,3, 4, 9]

9 in some

# lists have order
friends.sort() # this orders the list and modify it to be sorted. 
nums = [1, 2, 3,4, 5, 19]
len()
max()
min()
sum()
sum()/len() # average
  
  
numlist = list()
while True:
  inp = raw_input('Enter a number:')
  if inp == 'done': break
  value = float(inp)
  numlist.append(value)
  
average = sum(numlist) / len(numlist)
print(average)

# strings an lists
abc = 'with three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
for w in stuff:
  print w

# split looks at spaces, but you can use other stuff as well
thing = line.split(';')
print len(thing)

fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startwith('From'):continue
  words = line.split()
  print words[2]
# the double split pattern

words = line.split()
email = words[1]
pieces = email.split('@')
print pieces[1]
# you split the string twice and find what you are looking for


  





