fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = list()
count = 1
for line in fh:
    if count == 1:
        lst = line.split()
    else:
        lst2 = line.split()
        for word in lst2:
            if not word in lst:
                lst.append(word)
    count = count + 1

lst.sort()
print lst