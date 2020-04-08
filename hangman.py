import time
import Wordlist
import random
 # Creating wordlist
random_word = [
	"java", "C++", "Python", "Programming",
	"CSharp", "matlab", "artificial intelligence",
	"network", "hello world"
]
name = input("Hey! Whats your name?\n")

# Wait for a sec
time.sleep(1)

print("Hey! ", name, "Time to play hangman!")

time.sleep(1)

print(f"Hey {name} Start to guess")
time.sleep(0.5)

# Creating a word to guess
sec_word = random.choice(random_word)

guesses = ''

turns = 10

# Check if the turns are more than 0
while turns>0:
	
	failed = 0 # Counter starting with zero

	for char in sec_word: # loops through every char in the sec_word
		if char in guesses: # Condition Checks that if the character is in players guess
			print(char)
		else:
			# If the char is not found, print '_'
			print("_")

			# If failed increment the counter by 1
			failed += 1
	if failed == 0:
		print("\n")
		print(f"{name} won")
		break
	print()

	# Ask the user to guess a character
	guess = input("f{name} Guess the character: ")
	# Sets the player guess to guesses
	guesses += guess

	# Condition checks if the guess is not found in sec_word
	if guess not in sec_word:

		# then counter decreases with 1
		turns -= 1

		print("wrong")

		print(f"Turns Left: {turns}")

		if turns == 0:
			print("You Lose")
