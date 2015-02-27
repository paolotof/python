largest = None
smallest = None
while True:
  num = raw_input("Enter a number: ")
  if num == "done" : 
    break
  try:
    value = int(num)
  except:
    print "Invalid input"
    continue
  if smallest == None:
    smallest = value
  elif value < smallest: 
    smallest = value
  if largest == None:
        largest = value
  elif value > largest: 
    largest = value
        
print "Maximum is", largest
print "Minimum is", smallest