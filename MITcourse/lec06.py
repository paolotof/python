def keySearch(L, k):
    for elem in L:
        if elem[0] == k: return elem[1]
    return None

EtoF = {'bread': 'du pain', 'wine': 'du vin',\
        'eats': 'mange', 'drinks': 'bois',\
        'likes': 'aime', 1: 'un',\
        '6.00':'6.00'}

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word
    
def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' '\
                          + translateWord(word, EtoF)
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF)

##print translate('John eats bread')
##print translate('Eric drinks wine')
##print translate('Everyone likes 6.00')
# assumptions: 1) last word has no space, 2) there is a word between every word.
# why did you write a function:
# 1) to save code and be able to debug it
# 2) functional/modular abstraction: you only need to change the definition of this code only once. 
# This is divide and conquer: 1) split in small problems (are easy to solve) 2) the solution of small 
# problem can easily be combined to solve the big problem
# vidi en impera: divide and rule

# RECURSION is divide and conquer
# recursion definition base case (gives the direct answer) and inductive case (reduce to simpler
# version of same problem + some simple operations)
# Exponentiation with only multiplication
# b^n = b*b*b...
# b^n = b^n-1 if n > 0

def simpleExp(b, n):
    if n == 0:
	return 1
    else:
	return b * simpleExp(b, n-1)

# when you have a problem first think to how you can break it into small problems. 
# Tower of Hannoi problem.
# 

def Hannoi(n, frontStack, twoStack, spareStack):
    if n == 1:
	print 'move from ' + frontStack + ' to ' + twoStack
    else:
	Hannoi(n-1, frontStack, spareStack, twoStack)
	Hannoi(1, frontStack, twoStack, spareStack)
	Hannoi(n-1, spareStack, frontStack, twoStack)

# how long would it take to solve this problem.   

# palindrome: sentence that read the same from both sides. String of characters that read the 
# same front to back. Elba here i was saw i here Elba 


def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans

# 2 bases cases: one with length 1, one with length zero. 

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1]) # throw away first and last character

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

##print isPalindrome('Guttag')
##print isPalindrome('Guttug')
##print isPalindrome('Able was I ere I saw Elba')
##print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')

# this below is to check how the program digs into the problem
def isPalPrint(s, indent = '	'):
    print indent, 'isPalPrint called with', repr(s)
    if len(s) <= 1:
	print indent, 'About to return true from the base case'
        return True
    else:
	ans = s[0] == s[-1] and isPalPrint(s[1:-1], indent + indent) # throw away first and last character
	print indent, 'About to return', ans, 'for', s
        return ans


def isPalindromePrint(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPalPrint(toChars(s))

# fibonacci
# base case: if n == 0,1 = 1
# recursive case: f (n-2) + f(n-1)) # number of female at months n + number of female that were there the previous months

def fib(x):
    """assumes x an int >= 0
        Returns Fibonacci of x"""
    assert type(x) == int and x >=  0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        print ('fib of', i, '=', fib(i))
        
        
# relation if fib of n-1 close to infinity is the golden ration: 1 + root 5/2 
# number of petals on flowers is a fibonacci number. 