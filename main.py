water = 300
milk = 300
money = 0
coffee = 300
is_off = False
def count_coins():
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickels = int(input("How many nickels?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    global money
    money = float(quarters + dimes + nickels + pennies)
    print("You have put in " + str(money) + " dollars.")
    return money

while is_off == False:
    count_coins()
    choice = input("Would you like an espresso/cappuccino/latte?")

    if choice == "off":
        is_off = True
    elif choice == "report":
        print("Water: " + str(water) + " mL")
        print("Milk: " + str(milk) + " mL")
        print("Coffee: " + str(coffee) + "g")
        print("Money: $" + str(money))
        break;

    elif choice == "espresso":
        if water < 100:
            print("Not enough water")
        elif coffee < 15:
            print("Not enough coffee")
            is_off = True
        elif milk < 100:
            print("Not enough milk")
            is_off = True
        else:
            if money < 2:
                print("Not enough money for espresso, try again.")

            elif money >= 2:
                print("Here is your espresso, enjoy!")
                money -= 2
                water -= 50

    elif choice == "cappuccino":
        if water < 100:
            print("Not enough water")
            is_off = True
        elif coffee < 15:
            print("Not enough coffee")
            is_off = True
        elif milk < 100:
            print("Not enough milk")
            is_off = True
        else:
            if money < 1:
                print("Not enough money for cappuccino, try again.")

            elif money >= 2:
                print("Here is your cappuccino, enjoy!")
                money -= 2
                water -= 50

    elif choice == "latte":
        if water < 100:
            print("Not enough water")
        elif coffee < 15:
            print("Not enough coffee")
            is_off = True
        elif milk < 100:
            print("Not enough milk")
            is_off = True

        else:
            if money < 1:
                print("Not enough money for latte, try again.")

            elif money >= 2:
                print("Here is your latte, enjoy!")
                water -= 50
                money -= 2


