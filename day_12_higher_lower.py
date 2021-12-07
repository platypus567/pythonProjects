import random
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100. Can you guess it?")
difficulty = input("Game Mode: Easy or Hard?\n")
num_tries = 0
random_num = random.randint(1,100)
if difficulty == "hard":
     num_tries = 5
elif difficulty == "easy":
    num_tries = 10
print(f"You have {num_tries} tries.")
guess = ""
for i in range(num_tries):
    guess = int(input("Try to guess the number below:\n"))
    if guess == random_num:
        print(f"You win. The number was {random_num}")
        break;
    elif guess > random_num:
        print("Guess too high, try again.")
        num_tries -=1
        print(f"You have {num_tries} tries remaining.")
    elif guess < random_num:
        print("Guess too low, try again.")
        num_tries -=1
        print(f"You have {num_tries} tries remaining.")

