fhandle = open(filename, mode) # mechanism to handle the data we want to read
print fhandle

fhand = open('stuff.txt')

# The newline character \n. It counts as one character! 
# File processing

fhandle = open('mbox.txt')
for cheese in xfile:
  print cheese
  
#COunt number of line in file  
fhandle = open('mbox.txt')
count = 0
for line in fhandle:
  count = count + 1
  
print 'Line count', count

# you can also read the whole file, but you do not want to do that if the file is large
fhandle = open('mbox.txt')
inp = fhandle.read();
print len(inp)

# Searching through a file

fhandle = open('mbox.txt')
for line in fhandle:
  if line.startswith('From:'):
    print line
  
# print add a new line to each line that is prints. To handle this you use rstrip
fhandle = open('mbox.txt')
for line in fhandle:
  line = line.rstrip()
  if line.startswith('From:'):
    print line
  
# skipping pattern
fhandle = open('mbox.txt')
for line in fhandle:
  line = line.rstrip()
  # skip uninteresting lines
  #if not line.startswith('From:'):
    #continue
  # alternatively
  if not '@uct.ac.za' in line:
    continue
  # process our 'interesting lines'    
  print line

# prompting for a file nbame

fname = raw_input('Enter a file name: ')
fhandle = open(fname) 
count = 0
for line in fhandle:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were ', count, 'subject lines in ', fname

# you might want to have try and except for the file name
fname = raw_input('Enter a file name: ')
try:
  fhandle = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()
count = 0
for line in fhandle:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were ', count, 'subject lines in ', fname

##
# 7.1 Write a program that prompts for a file name, then opens that file and reads through 
# the file, and print the contents of the file in upper case. Use the file words.txt to 
# produce the output below.
#
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
#
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
#fh = open('words.txt')
for line in fh:
  line = line.rstrip()
  print line.upper()  
  
  
# 7.2 Write a program that prompts for a file name, then opens that file and reads through 
# the file, looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines and compute 
# the average of those values and produce an output as shown below.
#
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
# you are testing below enter mbox-short.txt as the file name.  
  
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
nLines = 0
confSum = 0.0
for line in fh:
    #if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:") :
#        print line
        nLines = nLines + 1
        atpos = line.find(':') + 1
        sppos = line.find('/n')
#        data = line[atpos:sppos]
#        print float(data)
        confSum = confSum + float(line[atpos:sppos])
#        print confSum
#   	print line
	    
        
#print "Done"
print 'Average spam confidence:', confSum/nLines

#
#	OR, with line skipping
#
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
nLines = 0
confSum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    nLines = nLines + 1
    atpos = line.find(':') + 1
    sppos = line.find('/n')
    confSum = confSum + float(line[atpos:sppos])
print 'Average spam confidence:', confSum/nLines

