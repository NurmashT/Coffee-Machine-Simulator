MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 5000,
    "milk": 3000,
    "coffee": 2000,
    "money": 0
} 
c = "cappuccino"
l = "latte"
e = "espresso"

should_continue = True

esperesso_ingr = list(MENU[list(MENU.keys())[0]].values())[0]
latte_ingr = list(MENU[list(MENU.keys())[1]].values())[0]
capuccino_ingr = list(MENU[list(MENU.keys())[2]].values())[0]

prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()


def sufficiency(ingredients):
    global should_continue
    global prompt
    if ingredients["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        should_continue = False
    elif prompt != e and ingredients["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        should_continue = False
    elif ingredients["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        should_continue = False
    
    else:
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]
        if prompt != e:
            resources["milk"] -= ingredients["milk"]
        calc_coins()
        print(f"Here is your {prompt} ☕. Enjoy! ")
    

def calc_coins():
    global should_continue
    global prompt
    print("please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    if total < MENU[prompt]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        should_continue = False
    else:
        total -= MENU[prompt]['cost']
        resources["money"] += MENU[prompt]['cost']
        print(f"Here is ${round(total, 2)} in change. ")


def machine():
    global should_continue
    global prompt
    while should_continue:
        if prompt == "off":
            should_continue = False
        elif prompt in list(MENU.keys()):
            if prompt == c:
                sufficiency(capuccino_ingr)
            elif prompt == e:
                sufficiency(esperesso_ingr)
            else:
                sufficiency(latte_ingr)
        elif prompt == "report":
            list_of_ingredients_left = list(resources.keys())
            list_of_values_left = list(resources.values())
            list_of_measurements = ["ml", "ml", "g", "$"]
            for i in range(len(list_of_ingredients_left)):
                print(f"{list_of_ingredients_left[i]}: {list_of_values_left[i]}{list_of_measurements[i]}")
        if should_continue:
            prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()


machine()
