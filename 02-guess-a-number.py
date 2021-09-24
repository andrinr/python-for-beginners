import random

start = 1
end = 6
actualNumber = random.randint(start, end)

userNumberGuess = int(input("Enter your number: "))

# Easy version
if (userNumberGuess == actualNumber):
    print("Sucess :)")

else:
    print("Wrong number, was: ", actualNumber)