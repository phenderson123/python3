import time

name = raw_input ("what is your name my friend?")

print "Hello, " + name, "It is hangman time people!!!"

print " "

time.sleep(1)

print "start guessing people!!!"
time.sleep(0.5)

word = "secret"

guesses = ""

turns = 10

while turns > 0:

    failed =0

    for char in word:

        if char in guesses:

            print char,

        else

            print "_"

            failed += 1

        if failed == 0

            print "you won!!"

            break

        print

        guess = raw_input ("take a guess on a character:")

        guesses += guess

        if guess not in word:

            turns -= 1

            print "wrong dude, so wrong.."

            print "You have", + turns, 'more guesses to go..'

            if turns == 0:

                print "you have so lost this game dude..."