import random

def main():
	# begins program

	# prints message to user
	print "Hello! I am what people say a guessing game! What is your name?"
	# gets input from user
	name = raw_input("Type your name here: ")
	# inserts name in another message to user
	print "%s, I'm thinking of a number between 1 and 100." % name
	# guess my number
	print "Try to guess my number."
	# the program will randomly choose a number in a range from 1 to 100
	my_num = random.randrange(1,100)
	# sets condition as True for the while loop
	condition = True
	# creates a counter
	count = 0
	# while loop for the guessing game
	while condition:
		# created a try and except for any error 
		# that may appear to prevent it from crashing
		try:
			# get input from user
			your_num = int(raw_input("Your guess? "))
			# if statements for number comparison
			if your_num >= 1 and your_num <= 100:
				if your_num > my_num:
					print "Your guess is too high. Try again."
					count += 1 # add to counter
				if your_num < my_num:
					print "Your guess is too low. Try again."
					count += 1 # add to counter
				if your_num == my_num:
					count += 1 # add to counter
					print "Horray! You got my guess in %d tries!" % count
					# set to False to break the while loop and end game
					condition = False
			else:
				# out of range
				print "Sorry, please give me a number between 1 and 100."
				count += 1 # add to counter
		except ValueError:
			print "That's not a number. Try again."

if __name__ == "__main__":
	main()