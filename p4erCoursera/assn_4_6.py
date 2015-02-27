# 4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 

def computepay(hours,rate):
  print "In compute pay hours=", hours, " rate=" rate
  pay = rate * hours
  if hours > 40:
	      pay = rate * (40) + rate * 1.5 * (h - 40)
  return(pay)
  #return 42.37

hrs = raw_input("Enter Hours:")
h = float(hrs)
r = 10.5
#p = computepay(10,20)
p=computepay(h,r)
#print "Pay",p
print p

## proper code:
try:
  inp = raw_input("Enter hours: ")
  hours = float(inp)
  inp = raw_input("Enter rate: ")
  rate = float(inp)
except
  print "Error, please enter numeric input"
  quit()

print "In the main code ", rate, hours
pay = computepay(rate, hours)
print "We are back", pay