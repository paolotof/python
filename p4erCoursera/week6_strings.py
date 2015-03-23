fruit = 'banana'
letter = fruit[1]
print letter
# a character too far

# len will tell us the length of the string. and not the length - 1

# you can loop through strings
fruit = 'bamama'
index = 0
while index < len(fruit):
  leter = fruit[index]
  print index, letter
  index = index + 1

# it can also be done in a loop through definite loop. This code is more elegant  
fruit = 'banana'
for letter in fruit:
  print letter
  
# looping and counting

word = 'banana'
count = 0
for letter in word:
  if letter == 'a':
    count = count + 1
print count

# looking deeper into IN
# 1 - the iteration variable iterates through the sequence (ordered set)
# 2 - the block (body) of code is executed once for each values in the sequence 
# 3 - the iteration variable moves through all of the values IN the SEQUENCE

# SLICING:
s = 'Monty Python'
print s[0:4]
# if you go further than the length of the string python stops. 

# STRING CONCATENATION	
# is done with the +, blanks aren't included so one needs to include them himself

# the IN operator in strings
# can be used to check if one string is in another string
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
# is a logical expression that returns true or false
if 'a' in fruit:
  print 'found it!'
  
# COMPARISON:
if word == 'banana':
  print 'all right bananas'
if word > banana:
  print 'wrod comes before banana'
elif word < banana:
  print 'word comes after banana'
else:
  print 'All right, bananas'
  
# string library is also built in  
# dir is a command that says what are the built-in methods of the string object
# it needs to be called on the already declared object not on the method:
# so it is greet = 'hello bob' dir(greet)
# and not dir(string), but dir(str) actually does work, string does not exist in python
# find is a built-in function to determine the string length
# upper() and lower() make the conversion if one wants everything in the same case
# replace 
# strip removes blanks, lstrip removes the left, rstrip removes the right ones.
# prefixes: startswith('letter, or word')
# from stephen.marquard@utc.ac.za sta jan
# example of parsing text
data  = 'stephen.marquard@utc.ac.za sta jan 5 09:14:16'
atpos = data.find('@')
sppos = data.find('', atpos) # we start at 21 and continue
host  = data[atpos+1 : sppos]

# Worked exercise 

# Write some code to parse lines of the form:
# X-DSPAM-Confidence: 0.8475
# use find and string slicing to extract the protion of hte string
# after the colon character and hten use the float function to convert
# the extracted string into a floating poitn number

# http://www.py4inf.com/code/mbox-short.txt

