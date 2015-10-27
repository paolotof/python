# print "hello world"

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
   if line.find('From:') >= 0:
       print line
        
# alternatively with regular expression
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line

## Searching for things at the beginning of the line:
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') >= 0:
       print line
        
# alternatively with regular expression
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print line


# the dot. 
# * Stars means any number of time
# ^X.*:
# match the start of the line followed by X and followed by any letter as needed up to :

# If we an to match any dash character after X
# ^X-\S+:
# \S character
# + as many times necessary

# []# enclose a set, e.g.: [0-9] one digit between 0 and 1
# [0-9]+ is one or more digits
# re.findall([0-9]+, x) # find all the situations matching. It returns a python list.
# [AEIOU]+ # one or more uppercase vowels (AEIOU). If nothing is found it returns an empty list.
# this search is greedy, so it will always return to longest match, if there are for example two characters statisfying the search pattern it will take all the characters up to the last one.
# If you need non-greedy matching: than you add a question mark:
# ^F.+?: - stats with an F ends with a column and get all characters in between 

# look for non blanks: 
# \S+@\S+ # find the @ sign and then find everything to the left and right side until you get a white space.
# fine tuning. 
y = re.findall('\S+@\S+', x)
# parenthesis indicate where to start or end with the search. If we use the parenthesis we want everything that matches
y = re.findall('~From (\S+@\S+)', x)# starts with From_ and then (\S+@\S+). And it will extract only the things between the parenthesis. Parenthesis allows to make a long regular expression and return only the part between parenthesis. 

# extract a host name: Look through the string until you find an @ sign, then the parenthesis says to start extracting. Then there is the square braket that says if the character is not a blank, then the * says match any of them: E.g. extract any non blank character from the @ sing to the the next blank character: '@([^ ]*)'
y = re.findall('@([^ ]*)', x) # alternatively

y = re.findall('^From .^@([^ ]*)', x) # starts with From_ (so that is From + space character) then followed by any number of characters, then find an #@ sign and then start extracting as long as there is a non-blank. What are you interesting in matching and what are you interested in extracting? 

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue # this is because findall returns a list, if there is no match it will just continue
    num = float(stuff[0])
    numlist.append(num)
    
print 'Maximum: ', max(numlist)

# to use the $ sign as dollar sign you prepend it with a backslash

# \$[0-9.]+ # real dollar sign followed by a digit or period, at least one or more



