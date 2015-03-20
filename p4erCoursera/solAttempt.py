fname = raw_input("Enter file name: ")
#fname
fh = open(fname)
#fh = open('romeo.txt')
lst = list()
count = 1
for line in fh:
    print count
    if count == 1:
        lst = line.split()
    else:
        lst2 = line.split()
        for word1 in lst:
            for word2 in lst2:
                if word1 == word2:
                    continue
                else:
                	lst.append(word2)
    count = count + 1
                
print lst.sort()        
    
#print line.rstrip()
