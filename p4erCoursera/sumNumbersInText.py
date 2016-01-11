import re

def sumIntInText(textfilename):
    hand = open(textfilename)
    num = 0
    for line in hand:
        line = line.rstrip()
        stuff = re.findall('([0-9]+)', line)
        if len(stuff) == 0 : continue
        for el in stuff:
          num = num + int(el)

    print 'Sum: ', num
    return num;


sumIntInText('regex_sum_42.txt')
sumIntInText('regex_sum_186379.txt')
