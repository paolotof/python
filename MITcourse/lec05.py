# to store data: touples, lists and dictionaries

## TOUPLES:


##Test = (1, 2, 3, 4, 5)
##print Test[0]
##print Test[1]

##x = 100
##divisors = ()
##for i in range(1,x):
##    if x%i == 0:
##        divisors = divisors+(i,) # this is to say it's a tuple of length 1
##print divisors

# slices of tuples : gives a range of values in the tuple
# tuples are immutable, so they cannot change the values.
# lists instead are mutable. 

#Techs = ['MIT', 'Cal Tech']
#Ivys = ['Harvard', 'Yale', 'Brown']
#Univs = []
#Univs.append(Techs) # mutates the list. The side effect
#print 'Univs =', Univs # it doesn't copy the list, it put the list itself
##
##Univs.append(Ivys)
##print 'Univs =', Univs
##for e in Univs:
##    print 'e =', e
##
##flat = Techs + Ivys # concatenate to new list
##print 'flat =', flat
##
##artSchools = ['RISD', 'Harvard']
##for u2 in artSchools:
##    if u2 in flat:
##        flat.remove(u2)
##
##print 'flat =', flat
##
# this orders the element in flat 
##flat.sort()
##print 'flat =', flat
##
# replacement of values. This is not an assignment, it modifies the object 
##flat[1] = 'UMass'
##print 'flat =', flat
#
# assignment specifies the bindings of names to objects mutation changes the values of objects
#
##L1 = [2]
##L2 = [L1, L1]
##print 'L2 =', L2
##L1[0] = 3 # this does not look like if you change L2. This is the beauty and the parlor of mutation
##print 'L2 =', L2
##L2[0] = 'a'
##print 'L2 =', L2
##
##L1 = [2]
##print 'L2 =', L2
####L2 = L1
####L2[0] = 'a'
####print 'L1 =', L1
####print 'L2 =', L2
##
##L1 = [2]
##L2 = L1[:]
##L2[0] = 'a'
##print 'L1 =', L1

##def copyList(LSource, LDest):
##    for e in LSource:
##        LDest.append(e)
##        print 'LDest =', LDest
##
##L1 = []
##L2 = [1,2,3]
##copyList(L2,L1)
##print L1
##print L2
##copyList(L1, L1) # this is an ALIAS: one object with two or more names.
##print L1 # this will crash, it will create confusion when you change one value and you forget to change what it is referring to. 

# Dictionary differs from a list because it isn't ordered and the indexes (keys) do not need to be integers but they can be any immutable type.

##EtoF = {'bread': 'du pain', 'wine': 'du vin',\
##        'eats': 'mange', 'drinks': 'bois',\
##        'likes': 'aime', 1: 'un',\
##        '6.00':'6.00'}
##print EtoF
##print EtoF.keys()
##print EtoF.keys
##del EtoF[1] # del can be used to delete
##print EtoF

# A dicts is a set of values and keys

##D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
##D1 = D
##print D1
##D[1] = 'uno'
##print D1
##for k in D1.keys():
##    print k, '=', D1[k]

# keys is a methods that return the keys of the dictionary.
# del can be used to delete
# del EtoF[1]

##def translateWord(word, dictionary):
##    if word in dictionary:
##        return dictionary[word]
##    else:
##        return word
    
##def translate(sentence):
##    translation = ''
##    word = ''
##    for c in sentence:
##        if c != ' ':
##            word = word + c
##        else:
##            translation = translation + ' '\
##                          + translateWord(word, EtoF)
##            word = ''
##    return translation[1:] + ' ' + translateWord(word, EtoF)

##print translate('John eats bread')
##print translate('Steve drinks wine')
##print translate('John likes 6.00')
##
##def keySearch(L, k):
##    for elem in L:
##        if elem[0] == k: return elem[1]
##    return None
