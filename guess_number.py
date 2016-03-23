import random
num=random.randint(0,100)

t=True
while t:
	guess=raw_input("^ ^please guess a number between 0 to 100:")
	guess_int=int(guess)
	if num>int(guess):
		print "too low!"
	if num<int(guess):
		print"too high!"
	if num==int(guess):
		print"You got it!Good job!*^_^*"
		t= False





