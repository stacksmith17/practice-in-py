#Create a random number guessing game with python.

import random 

num = random.randint(1,11)
attempt = 0 


while True:
    guess = int(input("please guess your number between(1-11):"))
    attempt += 1

    if guess < num :
        print ("too low")
    elif guess > num :
        print ("too high")
    else : 
        print (f"you guessed it right in {attempt} attempts ")
        break 

