Object oriented programming

movies = list()

movies.append()

keys = ['Title', 'Director', 'Rating', 'Runnign Time']

for item in movies:
  for key in keys:
    print key, ':', item[key]

Object orientation creates objects like this so that you know how to build it if you wouldn't have objects.

Object Oriented
A program is made up of many cooperating parts.

An object is code and data together.

A key aspect is that there are various kind of objects interacting.

Functions do not have separate part of data for each object.

Some part of the objects are hidden. It is a way to isolate complexity.

The complexity is divided.

Class: it is a template: a cookie cutter. It is what comes out of all these objects.
Method or Message: a defined capability of a class
Field or attribute a bit of data in a class
Object or Instance a particular instance of a class
Instance is the actual object that you are going to use.
Method is the way the class code is activated.

\Lecture 4 Simple python objects:

class is a reserved word. The name of the template is PartyAnimal.

class PartyAnimal:
  x = 0 # each PartyAnimal object has a bi of data
  # this is the code of PartyAnimal
  def party(self):
  # self allows the object to talk within itself
    self.x = self.x + 1
    print "So far", self.x

an = PartyAnimal() # create the PartyAnimal object

an.party() # calls PartyAnimal.party(an)
an.party() # so self becomes an alias of an
an.party()

Playing with dir() and type()

dir() command lists the capabilities,
these are methods intrinsic to the class

\Lecture 05 Object lifecycle

Constructor: set up some instance variables to have the proper initial values when the object is created.

class PartyAnimal:
  x = 0 # each PartyAnimal object has a bi of data

  def __init__(self):
    print "I am constructed"

  # this is the code of PartyAnimal
  def party(self):
  # self allows the object to talk within itself
    self.x = self.x + 1
    print "So far", self.x

  def __del__(self):
    print "I am destructed",self.x


The constructor and destructor are optional. The constructor is used to set up variables. The destructor is seldomly used.

Constructors can have parameters: e.g.:

class PartyAnimal:
  x = 0
  def __init__(self, nam):
    self.name = nam
    print self.name,"constructed"

  def party(self):
    self.x = self.x + 1
    print self.name,"party count",self.x

s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()

\Lecture 6 Inheritance (or extesion)

When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class

Another form of store and reuse

The new class (child) has all the capabilities of the old class (parent) and then some more.

Subclasses are a more specialized version of a class.

class FootbalFan(PartyAnimal)
  points = 0
  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print self.name,"points",self.points

j = FootbalFan("Jim")
j.party()
j.touchdown()

Summary
Object oriented programming is a very structured approach to code reuse.
We can group data and functionality together and create many independent instances of a class. 
