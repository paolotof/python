
import re
hand = open('mbox-short.txt')
sumVal = 0;
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
      # print x # not that x is still a list, so it must be indexed!
      sumVal = sumVal + float(x[0])
      count = count + 1

print sumVal/count

x = (5, 1, 3)

if (5, 0, 300) > x:
  print '1 is bigger than x'
if (6, 0, 0) > x:
  print '2 is bigger than x'
if (4, 100, 200) > x:
  print '3 is bigger than x'
if (0, 1000, 2000)  > x:
  print '4 is bigger than x'