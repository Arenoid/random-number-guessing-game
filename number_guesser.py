import random

n = random.randrange(1,10) #defining the range of the game
guess = int(input("Enter any number:")) #inputs any number
a=1

while n!=guess:
    if guess<n:
        print("Guess Too Low!")
        guess = int(input("Enter number again!"))
        a = a+1
    elif guess > n:
        print("Guess too high!")
        guess = int(input("Enter number again:"))
        a = a+1
    else:
        break;
    print(f"You guessed it right in {a} tries!")
        