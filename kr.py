import json


def create_json_files():
    # create units.json and prices.json for test
    with open("units.json", 'w') as outfile:
        json.dump({"bananas": [1, "kg"], "potatos": [4, "kg"], "beer": [3, "l"]}, outfile)

    with open("prices.json", 'w') as outfile:
        json.dump({"bananas": [1.25, "kg"], "potatos": [3.5, "kg"], "beer": [3, "l"]}, outfile)


def samm1_load_dicts(units_path, prices_path):
    with open(units_path, 'r') as rfile:
        units = json.load(rfile)
    with open(prices_path, 'r') as rfile:
        prices = json.load(rfile)
    return units, prices


def ask_product(units_dict):
    while True:
        user_choice_product = input("Type the name of the product: ")
        if samm3_is_exit(user_choice_product):
            break
        elif samm2_is_product_exist(units_dict, user_choice_product):
            break
        else:
            print("ERROR: Entered product is incorrect")
    return user_choice_product


def ask_amount(units_dict, prices_dict, product):
    while True:
        user_choice_amount = input("Enter the amount (price is {} / {}): ".
                                   format(prices_dict[product][0], prices_dict[product][1]))
        if samm3_is_exit(user_choice_amount):
            break
        elif samm2_is_amount_exist(units_dict, product, int(user_choice_amount)):
            break
        else:
            print("ERROR: Entered amount is incorrect")
    return user_choice_amount


def samm2_is_product_exist(dictionary, product):
    return product in dictionary


def samm2_is_amount_exist(dictionary, product, amount):
    return amount <= dictionary[product][0]


def samm3_is_exit(user_input):
    return user_input is ''


def samm1():
    units, prices = samm1_load_dicts("units.json", "prices.json")

    print("You can buy\n{}".format(list(units.keys())))

    while True:
        product = ask_product(units)
        if samm3_is_exit(product):
            break

        amount = ask_amount(units, prices, product)
        if samm3_is_exit(amount):
            break
        else:
            print("Please pay {}".format(int(amount) * prices[product][0]))
    print("Your shopping is finished")


def main():
    create_json_files()
    samm1()


if __name__ == '__main__':
    main()

