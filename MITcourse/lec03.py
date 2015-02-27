###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    #print 'current guess =', ans
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)

# Approximation: finding an answer which is good enough


###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##
##x = 25
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    ans += 0.00001
##    numGuesses += 1
##print 'numGuesses =', numGuesses
##if abs(ans**2 - x) >= epsilon:
##    print 'Failed on square root of', x
##else:
##    print ans, 'is close to square root of', x
##

# Bisection search: 1) cut the search space in half each iteration - start 
# with a guess (e.g. in the middle) and reduce the search space if the number 
# is smaller than the half, and on and on. This is log base 2 time faster. 
# So log number of values in that space.

x = 12345
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
   #print low, high, ans
   numGuesses += 1
   if ans**2 < x:
       low = ans
   else:
       high = ans
   ans = (high + low)/2.0
#print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

# Epsilon determines the size of the space. Does this program always work on positive values? 
# So when you write a fast code you need to make sure that is also gives you the right answer.
# If the values is not in the space of x then the algorithm will not work.

# If we want to write code that finds all different roots for all different numbers than we need 
# to transform our code into a function

##def withinEpsilon(x, y, epsilon):
##    """x, y, epsilon all ints or floats
##       returns true if x is within epsilon of y"""
##    return abs(x - y) <= epsilon
##
##if withinEpsilon(25, 26, 1):
##    print 'yes'
##else:
##    print 'no'
##
##if withinEpsilon(25, 26, 0.9):
##    print 'yes'
##else:
##    print 'no'

