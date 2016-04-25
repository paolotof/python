# http://en.wikipedia.org.wiki/Regular_Expression

# check out the cheatsheet. 

hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.find('From:') >= 0:
    print line
    
    
# using Regular_Expression
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('From:', line):
    print line

hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.startswith('From:') >= 0:
    print line

# using Regular_Expression
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^From:', line):
    print line
    
# wild-card characters
# the dot character matches any character

# if you add asterisks the character is looked for any number of times

^X.*:
  
#   starts with X followed by any character any number of times

# but you could do:
  ^X-\S+:
#match any start of the line with X followed by any non-whitespace character one or more times and ends with  a column 


# extracting data: 

re.findall('[0-9]+', line)
# one of more digits any time that it cans. it returns a python list of strings. It can return a zero length string if it returns an empty match.

# Greedy matching:
# the repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

y = re.findall('^F.+:', line)
# first character in the match is an 'F', one or more characters, Last character in the match is a ':'
y = re.findall('^F.+?:', line) # don't be greedy, just get the first one that matches the criteria

# extract e-mail address from string:

\S+@\S+ # at least one non-whitespace character around the '@' character

re.findall('^From (\S+@\S+)', line) # only the parenthesis part is extracted. This is a more narrow search because there has to be 'From ' in front.

# extracting a host name using find and string slicing:

data = 'From stephen.marquant@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find('', atpos)
print sppos
host = data[atpos+1 : sppos]
print host

# double split version:
words = line.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

# Regular_Expression
re.findall('@([^ ]*)', line)
# find '@', and extract all non blank-characters after the @ sign
# or even better:
re.findall('^From .*@([^ ]*)') # match is much more narrow

# spam confidence

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
  line = line.rstrip()
  stuff = re.findall('^X-DSPAM-Confidence:([0-9.]+)' , line)
  if len(stuff) != 1 : continue
  num = float(stuff[0])
  numlist.append(num)
  
print 'Maximum: ', max(numlist)

