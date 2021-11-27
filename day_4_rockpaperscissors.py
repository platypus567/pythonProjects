import random
player_input = input("Welcome to Rock Paper Scissors. Input 0 for Rock, 1 for Paper, 2 for Scissors.\n")
computer_move = random.randint(0,3)
if str(player_input) == "0":
    if computer_move == 1:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You chose Rock, Computer chose Rock. Tie.")
    elif computer_move == 2:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You chose Rock, Computer chose Paper. You lose.")
    elif computer_move == 3:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You chose Rock, Computer chose Scissors. You win.")
elif str(player_input) == "1":
    if computer_move == 1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You chose Paper, Computer chose Rock. You Win.")
    elif computer_move == 2:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You chose Paper, Computer chose Paper. You tie.")
    elif computer_move == 3:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You chose Paper, Computer chose Scissors. You Lose.")

elif str(player_input) == "2":
    if computer_move == 1:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You chose Scissors, Computer chose Rock. You Lose.")
    elif computer_move == 2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        
        print("You chose Scissors, Computer chose Paper. You Win.")
    elif computer_move == 3:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You chose Scissors, Computer chose Scissors. You Tie.")
