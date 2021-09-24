import random
import commonThings

index = int(random.randint(0, len(commonThings.list)))

word = commonThings.list[index]

currentIndex = 1

while (currentIndex <= len(word)):
    print("Prefix is: ", word[0: currentIndex])
    guess = input("Make a guess! ")

    currentIndex += 1
    if (guess == word):
        print("sucess!")
        break
    else:
        print("Not quiet. Here is the next hint:")
