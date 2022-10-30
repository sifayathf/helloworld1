import random

highest = 10
answer = random.randint(1,highest)
print(answer)
passcount=1
guess =5
passcount+=2
print('passcount' ,passcount)

if guess < answer and passcount == 2:
    print("Please guess higher", passcount)
    guess = int(input())

elif guess > answer and passcount == 2:
    print("Please guess lower", passcount)
    guess = int(input())

else:
    print("You have guessed it wrong")
    exit

