import random
secret = random.randint(1, 30)
guess = -1

for i in range (5):

    print "You have", 5-i, "tries left."
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number " + str(secret) + " :)"
        break
    else:
        print "Sorry, your guess is not correct... Secret number is not " + str(guess)
        if guess < secret:
            print "Try a higher number."
        else:
            print "Try a lower number."
        if i==4:
                print "You've run out of tries."