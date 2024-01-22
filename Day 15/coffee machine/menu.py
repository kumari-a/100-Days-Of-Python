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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resource(item):
    for requirement in item:
        if resources[requirement]<item[requirement]:
            print('Sorry not enough ingredients')
            return False
    return True


def convert_money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(money, cost):
    if money >= cost:
        global profit
        profit+=cost
        change = round(money-cost,2)
        print(f"Here is your change ${change}.")
        return True
    else:
        print("Sorry not enough money.")
    return False

def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy you {drink_name}.☕")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resource(drink["ingredients"]):
            payment = convert_money()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])