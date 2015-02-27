# definig a function in python is 
def hello():
  print 'hello'
  print 'fun'
  
# 2 types of functions: 1) built-in, 2) self-defined.
# the result is going to be assigned to a variable
# input - processing - output
# float, type do type conversion or check the value
# string conversion - int() -> converts string to integer
# defining the function only groups a code of commands, but does not execute the code
# function calls or invocation is when you call a function to do something 
# arguments of the function are values passed to the function to do something with it

def greet(lang):
  if lang == 'es':
    print 'Hola'
  elif lang == 'fr':
    print 'Bonjour'
  else:
    print 'Hello'

greet('en')

# function are used to do something and RETURN a value:

def greet():
  return "Hello"

#Return defines the end of a function and also the value that should be return
def greet(lang):
  if lang == 'es':
    return 'Hola'
  elif lang == 'fr':
    return 'Bonjour'
  else:
    return 'Hello'

# this is how you would call them  
print greet('en')  

# the function that produces output are fruitful, the one that do not produce values are void (non-fruitful)
# arguments parameters and results. parameters can also be defined inside of the function definition.
# why would I use functions? This is when you do things over and over again.
# Argument: value passed to the function as its input
# Parameter: variable used in the function definition. It's a handle which allows the code in the function to access the arguments for a particular function invocation. 
print "Question 4"
def thing():
    print 'Hello'
 
print 'There'

print "Question 6"
def func(x) :
    print x

func(10)
func(20)

print "Question 7"
def stuff():
    print 'Hello'
    return
    print 'World'

stuff()

print "Question 8"
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
 
print greet('fr'),'Michael'

print "Question 9"
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print x