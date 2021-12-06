
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     


def deal_card():

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score, dealer_score):
  if user_score > 21 and dealer_score > 21:
    return("Player busts.")
  elif user_score == dealer_score:
    return("Push. Game ties.")
  elif user_score > 21:
    return("Player busts.")
  elif dealer_score > 21:
    return("Dealer busts.")
  elif user_score == 0:
    return("Player has blackjack. Player wins.")
  elif dealer_score == 0:
    return("Dealer has blackjack. Dealer wins.")
  elif user_score > dealer_score:
    return("User has greater hand. Player wins.")
  elif dealer_score > user_score:
    return("Dealer has greater hand. Dealer wins.")
  
def game():
  game_is_over = False
  user_cards = []
  dealer_cards = []
  print(logo)
  for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  while not game_is_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"   Your hand is {user_cards}, the dealers card is {dealer_cards[0]}.")
    if user_score > 21 or user_score == 0 or dealer_score == 0:
      game_is_over = True
    else:
      hit_or_stand = input("Will the player hit or stand? \n")
      if hit_or_stand == "hit":
        user_cards.append(deal_card())
      else:
        game_is_over = True
  while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)
  print(f"Your final hand: {user_cards}. Hand Score: {user_score}.")
  print(f"Dealer final hand: {dealer_cards}. Dealers score: {dealer_score}.")
  print(compare(user_score,dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  print ("\n" * 100)
  game()


