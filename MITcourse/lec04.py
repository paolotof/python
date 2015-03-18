
# search the place where the bug is
x = 0.5
epsilon = 0.01
low = 0.0
high = max(x, 1.0)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
   print 'ans =', ans, 'low =', low, 'high =', high
   if ans**2 < x:
       low = ans
   else:
       high = ans
   ans = (high + low)/2.0
print ans, 'is close to square root of', x

## in general you want to make the code as shorter as possible. 
## Productivity is done measuring the functionality of a program, not how many line it is
# Functions creates:
# 1 - decomposition - creates structure breaking up the program in modules which are 1) self-contained and 2) reusable
# 2 - abstraction - suppresses details. Allow to use code as black box, you use the functionality but you don't care of how it does it.
# important modules in python are classes and functions

def withinEpsilon(x, y, epsilon):
   """x,y,epsilon ints or floats.  epsilon > 0.0
      returns True if x is within epsilon of y"""
   return abs(x - y) <= epsilon

# function has a name, parameters and body. In the body you can write anything and return, which is the value that we are going to return.
# writing a function without 'return' returns 'None'

# function invocation:
print withinEpsilon(2,3,1)
val = withinEpsilon(2,3,0.5)
print val

def f(x):
  x = x + 1
  print 'x =', x
  return x

x = 3
z = f(x)
print 'z =', z
print 'x =', x

# When you can a function the formal parameter (x) is bound to the value of the actual parameter, x.
# When you enter a function a new scope (a mapping from name to objects) is created

# assert is a special case, it continues running if the output of the assert is true, stops if it is false
# Assert is defensive programming, it's used to check whether the values entered are proper. 

##def f1(x):
##   def g():
##       x = 'abc'
##  	 # assert False # this is the code to check assertion error
##   x = x + 1
##   print 'x =', x 
##   g()
##   assert False # if you are running for this remove the line 56
##   return x

# go to the debug and call the stack viewer. The stack works last in first out (LIFO). Which function exists in the stack depends on which functions were called first.



# using functions to find roots:

##x = 3
##z = f1(x)

##def isEven(i):
##    """assumes i a positive int
##       returns True if i is even, otherwise False"""
##    return i%2 == 0

##def findRoot(pwr, val, epsilon):
##    """assumes pwr an int; val, epsilon floats
##       pwr and epsilon > 0
##       if it exists,
##          returns a value within epsilon of val**pwr
##          otherwise returns None"""
##    assert type(pwr) == int and type(val) == float\
##           and type(epsilon) == float
##    assert pwr > 0 and epsilon > 0
##    if isEven(pwr) and val < 0:
##          return None
##    low = -abs(val)
##    high = max(abs(val), 1.0)
##    ans = (high + low)/2.0
##    while not withinEpsilon(ans**pwr, val, epsilon):
##        #print 'ans =', ans, 'low =', low, 'high =', high
##        if ans**pwr < val:
##           low = ans
##        else:
##           high = ans
##        ans = (high + low)/2.0
##    return ans

##def testFindRoot():
##    """x float, epsilon float, pwr positive int"""
##    for x in (-1.0, 1.0, 3456.0):
##        for pwr in (1, 2, 3):
##            ans = findRoot(pwr, x, 0.001)
##            if ans == None:
##                print 'The answer is imaginary'
##            else:
##                print ans, 'to the power', pwr,\
##                'is close to', x 

#testFindRoot()

# strings: 
# str() convert a number to a string 
# slicing s[0:1], or s[0:2]
# tuples will be discussed in the recitation

##sumDigits = 0
##for c in str(1952):
##    sumDigits += int(c)
##print sumDigits

##x = 100
##divisors = ()
##for i in range(1, x):
##    if x%i == 0:
##        divisors = divisors + (i,)
##
##print divisors
##print divisors[0] + divisors[1]
##print divisors[2:4]

