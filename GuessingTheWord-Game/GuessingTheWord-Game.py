import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['yog', 'sarvesh', 'kshitij', 'itssuru', 'purvesh', 'studioslegends', 'sanchit',
         'sameer', 'varun', 'vivek', 'tejas', 'suyog', 'vedant', 'vedang', 'brawlstars',
         'clashofclans', 'pubg', 'apexlegends', 'ksins', 'facebook', 'bollywood',
         'hollywood', 'ankit', 'computer', 'avneet', 'amongus', 'instagram', 'shraddha',
         'asus', 'msi', 'dog', 'nagpur', 'pune', 'mumbai', 'gym']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 5

while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
