from art import logo, vs
from game_data import data
import random
from replit import clear
counter = 0
def random_choice():
  return random.choice(data)
def take_data(account):
  name = account["name"]
  followers = account["follower_count"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"
def answer_check(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
def game():
  game_over = False
  score = 0
  choice_a = random_choice()
  choice_b = random_choice()
  print(logo)
  while game_over == False:
    choice_a = choice_b
    choice_b = random_choice()
    while choice_a == choice_b:
        choice_b == random_choice()

    print("Compare A: " + take_data(choice_a))
    print(vs)
    print("To B: " + take_data(choice_b))
    guess = input("Who do you think has more followers?").lower()
    a_followers = choice_a["follower_count"]
    b_followers = choice_b["follower_count"]
    is_correct = answer_check(guess,a_followers,b_followers)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"Correct! Current score: {score}")
    else:
      game_over = True
      print(f"You failed. Final score: {score}")
game()

    




#loop through names in data and print string for name, country, and description

#for item in data:
  #print("Name: " + item["name"] + "\nFollowers: " + str(item["follower_count"]) + "\nDescription: " + item["description"] + "\n \n")

    #while game_over == False:
      

