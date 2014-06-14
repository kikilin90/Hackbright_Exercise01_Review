import random

def main():

	print "Hello! I am what people say a guessing game! What is your name?"

	name = raw_input("Type your name here: ")

	print "%s, I'm thinking of a number between 1 and 100." % name

	print "Try to guess my number."

	my_num = random.randrange(1,100)

	condition = True

	count = 0

	while condition:
		try:
			your_num = int(raw_input("Your guess? "))
			if your_num >= 1 and your_num <= 100:
				if your_num > my_num:
					print "Your guess is too high. Try again."
					count += 1
				if your_num < my_num:
					print "Your guess is too low. Try again."
					count += 1
				if your_num == my_num:
					count += 1
					print "Horray! You got my guess in %d tries!" % count
					condition = False
			else:
				print "Sorry, please give me a number between 1 and 100."
				count += 1
		except ValueError:
			print "That's not a number. Try again."

if __name__ == "__main__":
	main()