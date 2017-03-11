
print "Welcome to the FizzBuzz game!"
exit_number = raw_input("Enter a number between 1-100 to define end point of game: ")
print exit_number
print

for i in range(int(exit_number) + 1):
    fizz = i % 3
    buzz = i % 5

    if i == 0:
        print "Start"
    elif fizz == 0 and buzz != 0:
        print "Fizz"
    elif buzz == 0 and fizz != 0:
        print "Buzz"
    elif fizz == 0 and buzz == 0:
        print "FizzBuzz"
    else:
        print i

