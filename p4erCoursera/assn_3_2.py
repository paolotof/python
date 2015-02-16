# score = float(raw_input('Enter a score between 0.0 and 1.0'))
# this however handles the wrognly entered inputs
scoreStr = raw_input('Enter a score between 0.0 and 1.0')
try:
  score = float(scoreStr)
except:
  score = -1

if score > 1.0:
	print 'Score entered is invalid'
elif score >= .9:
	print 'A'
elif score >= .8:
	print 'B'
elif score >= .7:
	print 'C'
elif score >= .6:
	print 'D'
elif score < .0:
	print 'Score entered is invalid'
else :   
	print 'F'
