#Fizzbuzz Challenge

#if no. is divisible by 3, print "Fizz"
#if no. is divisible by 5, print "Buzz"
#if no. is divisible by both , print "FizzBuzz"


for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}:FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}:Fizz")
    elif i % 5 == 0:
        print(f"{i}:Buzz")
    else:
        print(f"{i}:Is neither divisible by 3 or 5")

