"""File contains class and methods for shopify
   This is meant for just processing users orders, display their orders and update catalogue
   Catalogue does not update at the moment.
"""
import os.path
import json
from datetime import datetime
from time import sleep

order_list = []  # Empty list use in place_order() to collate users order in else block and dump in order.json file


class Order:
    def __init__(self):
        self.name = ""
        self.item_name = ""
        self.item_price = 1
        self.quantity = ""

    def place_order(self, name, item, quantity):
        """method that processes user order receiving user's name,item and quantity
            checks if order item and quantity details are available in catalogue
            then stores order to order.json file
        """
        try:
            if not os.path.exists("catalogue.json"):  # checks if admin has created catalogue file
                print("Catalogue file does not exist, kindly create catalogue")
            elif os.path.getsize("catalogue.json") == 0:
                print("Catalogue is empty")
            else:
                with open("catalogue.json", "r") as file:  # open catalogue file containing
                    data = json.load(file)  # load json file to data
                    item_name_list = []  # create an empty item list to collect item names for conditional testing

                    for products in data["items"]:
                        '''For loop to get all item names from catalogue and place them in empty list(item_name_list)'''
                        self.item_name = products["name"]
                        item_name_list.append(self.item_name.lower())

                    for product in data["items"]:
                        """Loop to get item_name and quantity from catalogue, retain user name, assign
                           values to self(individual object) and tests for various condition to validate user order
                          """
                        self.name, self.item_name, self.quantity = name, product["name"], product[
                            "quantity"]  # assign values for testing
                        #print(self.name, self.item_name, self.quantity)

                        if item.lower() not in item_name_list:  # test if user's ordered item name is not in item name in catalogue
                            print(item, "is not in catalogue")  # prints if not present
                            break  # terminate loop

                        elif not name:  # checks if user does not enter his/her name for order alignment
                            print("Kindly enter a name so as to identify your order while processing")
                            break  # terminate loop
                        elif not item:  # test if user enters no value for item name
                            print("Item cannot be empty")
                            break  # terminate loop
                        elif not quantity:  # test if user enters no quantity
                            print("Quantity cannot be empty")
                            break  # terminate loop
                        else:
                            """Else code block is used to dump user order details available in catalogue into order json file"""
                            if item.lower() == self.item_name.lower():  # checks if ordered item is in catalogue
                                self.name, self.item_name, self.quantity = name, product["name"], product["quantity"]
                                print(item, "is in catalogue")
                                if quantity > int(
                                        self.quantity):  # test if quantity ordered is greater than available quantity in catalogue
                                    print(self.quantity)
                                    print("Quantity ordered is higher than stock available")
                                    break
                                try:
                                    with open("order.json", "w") as order_file:
                                        time = datetime.now().strftime("%Y-%m-%d %H:%M")
                                        order_data = {"name": self.name, "item": self.item_name, "quantity": quantity,
                                                      "time": time} # store user order
                                        order_list.append(order_data)  # append user order for dumping to JSON file
                                        json.dump(order_list , order_file,
                                                  indent=4)  # store user order as dict appended to a list
                                        sleep(0.5)
                                        self.quantity -= quantity
                                        print("Order placed successfully")
                                except Exception as e:
                                    print(e)
                                break
        except Exception as e:
            print(e)

    def display_order(self, name):
        """Method displays user order and amount to pay"""
        try:

            if not os.path.exists("order.json"):
                print("order file does not exist")
            elif os.path.getsize("order.json") == 0:
                print("Order file is empty")
            else:
                with open("order.json", "r") as order_file, open("catalogue.json", "r") as cat_file:
                    line = json.load(order_file)
                    name_list = []
                    for detail in line:
                        self.name = detail["name"]
                        name_list.append(self.name.lower())
                    # print(name_list)
                    for detail1 in line:
                        self.name, self.item_name, self.quantity, time = detail1["name"], detail1["item"], detail1[
                            "quantity"], detail1["time"]
                        # print(self.name, self.item_name, self.quantity)
                        if not name or (type(name) != str):
                            print("Kindly enter a name so as to process your order using your name")
                            break
                        elif name.lower() not in name_list:
                            print(name, "has not placed an order")
                            break
                        else:
                            if name.lower() == detail1["name"].lower():
                                self.name, self.item_name, self.quantity, time = detail1["name"], detail1["item"], detail1[
                                    "quantity"], detail1["time"]
                                # print(self.name, self.item_name, self.quantity,time)
                            else:
                                continue
                            cat_line = json.load(cat_file)
                            if not cat_line:
                                print("catalogue is empty")
                            for cat_detail in cat_line["items"]:
                                if self.item_name.lower() == cat_detail["name"].lower():
                                    cat_item_price = cat_detail["price"]
                                # if order_item_name == cat_item_name:
                                #     self.item_price = cat_item_price
                            print("Your Order details are as follows:")
                            print("Order was placed on", time)
                            print("Name:", self.name)
                            print("Item Name:", self.item_name)
                            print("Quantity Ordered:", self.quantity)
                            print("Total Price to pay on delivery: #", cat_item_price * int(self.quantity))
                            break
        except Exception as e:
            print(e)

    def catalogue(self):
        if not os.path.exists("catalogue.json"):
            print("Catalogue file does not exist")
        elif os.path.getsize("catalogue.json") == 0:
            print("Catalogue is empty")
        else:
            print("Available Items in our catalogue:")
            try:
                with open("catalogue.json", "r") as file:
                    data = json.load(file)
                    if not data:
                        print("No Catalogue available in file")
                        return
                    item_list = 1
                    for item in data["items"]:
                        self.item_name, self.item_price, self.quantity = item["name"], item["price"], item["quantity"]
                        print(f"{item_list}) Item Name:", self.item_name, f"Price:#{self.item_price}", "Qty left:",
                              self.quantity, "\n")
                        item_list += 1
                        # continue
            except Exception as e:
                print(e)


def introduction():
    print("Welcome to Shopify")
