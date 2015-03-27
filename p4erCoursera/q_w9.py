#stuff = dict()
#print stuff['candy']

#stuff = dict()
#print stuff.get('candy',-1)

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

counts[key] = (key in counts) + 1
counts[key] = counts.get(key,-1) + 1
counts[key] = key + 1
counts[key] = counts.get(key,0) + 1
counts[key] = (counts[key] * 1) + 1 