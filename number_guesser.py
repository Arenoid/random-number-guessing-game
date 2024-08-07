import random

diff_easy = random.randrange(1, 10)
diff_medium = random.randrange(1, 20)
diff_hard = random.randrange(1, 50)  # defining the range of the game



diff_level = int(input("Enter difficulty:\n 1: Easy(1-10) \n 2: Medium(1-20) \n 3: Hard(1-50):"))

a = 0

#Easy Difficulty
if diff_level == 1:
    g1 = int(input("Enter the number:"))
    while diff_easy != g1:
        if diff_easy < g1:
            print("Guess too high!")
        else:
            print("Guess too low!")
        g1 = int(input("Enter the number:"))
        a += 1
    print(f"Congrats! You guessed it in {a} tries ")
#Medium difficulty

if diff_level == 2:
    g2 = int(input("Enter the number:"))
    while diff_medium != g2:
        if diff_medium < g2:
            print("Guess too high!")
        else:
            print("Guess too low!")
        g2 = int(input("Enter the number:"))
        a += 1
    print(f"Congrats! You guessed it in {a} tries ")

#hard difficulty
if diff_level == 3:
    g3 = int(input("Enter the number:"))
    while diff_hard != g3:
        if diff_hard < g3:
            print("Guess too high!")
        else:
            print("Guess too low!")
        g3 = int(input("Enter the number:"))
        a += 1
    print(f"Congrats! You guessed it in {a} tries ")
    
  
  