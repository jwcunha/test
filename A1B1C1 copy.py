import sys

#alpha = 'ABCDEFGH'

def a1b1c1(max):
	e = 1
	cap = 1
	while e <= max:
		while cap <= 12:
			for letter in alpha:
				print letter + str(cap)
			cap += 1
	cap = 1
	e += 1

def a1a2a3(alpha):
	e = 1
	cap = 1
	for letter in alpha:
		while cap <=12:
			print letter + str(e)
			e+=1
			cap += 1
		cap = 1
		e = 1


#x = sys.argv[1]

print a1a2a3('ABCDEFGH')
