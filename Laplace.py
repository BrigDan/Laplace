#Real Numbers

# Even Numbers
def isEven(val):
    return val % 2 == 0

# Odd Numbers
def isOdd(val):
	return val % 2 != 0

# Prime and Composite Numbers

def isPrime(val):
	# Counter
	# Any number that is lower than 2 cannot be false
	i = 2
	# Ensure that the program doesn't loop over the number we're looking for
	while val > i:
		#If the number divisible by 2 returns 0 remainder it is not prime.
		if val % i == 0 and i != val:
			return False
			break
		#Incrament Counter
		i+=1
	else:
		#Otherwise its Prime
		return True

def isComposite(val):
	# Counter
	# Any number that is lower than 2 cannot be false
	i = 2
	# Ensure that the program doesn't loop over the number we're looking for
	while val > i:
		#If the number divisible by 2 returns 0 remainder it is not prime.
		if val % i == 0 and i != val:
			return True
			break
		#Incrament Counter
		i+=1
	else:
		#Otherwise its Prime
		return False

def divisibilityTest(val,by):
	return val % by == 0
