n = 5
while n > 0
  print n
  n = n-1
print "Blastoff!"
print n

# infinite loops never ends
# loops that never runs - zero trips loops

# indefinite loops
#breaking out of a loops
# 1 - break
while True:
  line = raw_input('>')
  if line == 'done':
    break
  print line
print 'Done!'
# 2 - continue  
while True:
  line = raw_input('>')
  if line[0] == '#':
    continue # stop iteration start from beginning
  if line == 'done':
    break
  print line
print 'Done!'

# definite loops
for i in [5,4,3,2,1]:
  print i
  
print 'Blastoff!'

# this is a list: [5,4,3,2,1], this is also a list:
friends = ['Joseph','Mary', 'Jesus']
for friend in friends:
  print 'Happy new year', friend
print 'Blastoff!'  

# The iteration variable in has different functions:
# - it iterates through the sequence
# - it executes once the 'block - body' of code for each value in the sequence 
# - it moves through all the values in the sequence

#definite loops iterates through the numbers of a set
# loop idioms

# making smart loops (e.g. find the largest number)
largest_so_far = -1
print 'Before ', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num > largest_so_far:
    largest_so_far = the_num
  print largest_so_far, the_num
print 'After ', largest_so_far

# counting in a loop
largest_so_far = -1
zork = 0
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num > largest_so_far:
    zork = zrok + 1
    largest_so_far = the_num
print largest_so_far, zork

# summing in a loop
zork = 0
print 'Before ', zork
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num > largest_so_far:
    zork = zork + the_num
    print zork, the_num
print 'After ', zork

# average in a loop
count = 0
zork = 0
print 'Before ', count, zork
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num > largest_so_far:
    count = count + 1
    zork = zork + the_num
    print zork, count, the_num
print 'After ', zork, count, zork/count

# filtering in a loop
print 'Before'
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num > 20:
    print the_num
print 'After'  

# searching using a boolean value
found = False
print ' Before', found
for the_num in [9, 41, 12, 3, 74, 15]:
  if the_num == 3:
    found = True
    break
  print found, the_num
  
print 'After', found  


smallest = None
print 'Before '
for the_num in [9, 41, 12, 3, 74, 15]:
  if smallest is None:
    smallest = the_num
  elif the_num < smallest
    smallest = the_num
  print smallest, the_num
print 'After, ', smallest
  
# 'is' and 'is not' - it's use for True, False or None, otherwise always use ==. Is can be used in logical expressions 



