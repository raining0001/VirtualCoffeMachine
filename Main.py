from art import logo, menu
from value import coins , coins_val
from drinks import recepies, price
from stock import report


def user_money():
    print("Please insert coins.")
    coins["quarter"] = int(input("How many quarters?: "))
    coins["dime"] = int(input("How many dimes?: "))
    coins["nickel"] = int(input("How many nickels?: "))
    coins["penny"] = int(input("How many pennies?: "))
  
    global user_sum
    user_sum = sum(coins_val[key] * value for key, value in coins.items())

def check_resources(user):
    for key, value in recepies[user].items():
        if value > report["resources"][key]:
            print(f"Sorry not enough resources")
            return False
    return True

def drink_change():
    global machine_sum
    change = user_sum - price[user]["money"]
    machine_sum += price[user]["money"]
    print(f"Here is {change} in change.")
    print("Here is your latte, Enjoy!")

machine_sum = sum(report["money"].values())


print(logo)
print(menu)

while True:
    user = input("What would you like to drink? ").lower()
    if user == 'report':
        print(report)
    elif check_resources(user):
        user_money()
        if user_sum > price[user]["money"]:
            drink_change()
        elif user_sum == price[user]["money"]:
            machine_sum += user_sum
            print("Here is your latte, Enjoy!")
        else:
            print("Sorry not enough money. Money refunded")
        break
