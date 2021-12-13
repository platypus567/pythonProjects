from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while is_on == True:
  menu.__init__()
  money_machine.__init__()
  coffee_machine.__init__()
  choice = input("Select from " + menu.get_items() +"\n")
  if choice == "report":
    coffee_machine.report()
    money_machine.report()
  else:
    selected = menu.find_drink(choice)
    if coffee_machine.is_resource_sufficient(selected):
      if money_machine.make_payment(selected.cost) == True:
        coffee_machine.make_coffee(selected)

  
  
# if choice == "report":
 #   coffee_machine.report()
  #elif choice == "cappuccino" and coffee_machine.is_resource_sufficient(menu.find_drink()):
   # coffee_machine.make_coffee(MenuItem)