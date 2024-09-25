import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    user_input = " "
    while user_input != "off":
        user_input = input("What would you like? (small/ medium/ large/ off/ report): ")
        if user_input == "off":
            break

        elif user_input == "report":
            bread = resources["bread"]
            ham = resources["ham"]
            cheese = resources["cheese"]
            print(f"Bread: {bread} slice(s)")
            print(f"Ham: {ham} slice(s)")
            print(f"Cheese: {cheese} pound(s)")

        elif user_input in recipes:
            sandwich_size = recipes[user_input]
            ingredient_list = sandwich_size["ingredients"]
            cost = sandwich_size["cost"]

            check_resources = sandwich_maker_instance.check_resources(ingredient_list)
            if check_resources:
                print("Please insert coins.")
                coins_amount = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins_amount, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredient_list)

        else:
            print("")


if __name__ == "__main__":
    main()
