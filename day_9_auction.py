
clearConsole = lambda: print('\n' * 150)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders = []
bids = {}
are_there_bidders = True


def highest_bidder(bid_record):
  winner = ""
  high_bid = 0
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > high_bid:
      high_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {high_bid}")




while are_there_bidders == True:
  name = input("What is your name?\n")
  bid = int(input("What is your bid price in dollars?\n"))
  bids[name] = bid

  question = input("Are there more bidders?\n")
  if question.lower() == "yes":
    clearConsole()
  elif question.lower() == "no":
    highest_bidder(bids)
    break;


    

