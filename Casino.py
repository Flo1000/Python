# Casino game - guess the right number between 1-9

win_number = 3
print "Welcome to the guess the right number game!"
guess_number = raw_input("Enter a number between 1 and 9: ")
print "Your choice is: " + guess_number

# Validate input
if int(guess_number) >9:
    print ("Not a valid input. Try again.")
    guess_number = raw_input("Enter a number between 1 and 9: ")
if int(guess_number) < 1:
    print ("Not a valid input. Try again.")
    guess_number = raw_input("Enter a number between 1 and 9: ")

# Result announcement
if int(guess_number) == int(win_number):
    print "Congratulations!!! You won!!!"
else:
    print "Sorry, wrong number. The winning number would have been:" , win_number