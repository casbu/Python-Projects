from ProductObjects import Product, ProductInventory, Basket
import FileIO


def display_menu():
    print("Menu Options")
    print("products  - show all available products")
    print("basket    - show products in the shopping basket")
    print("add       - add a product to the basket")
    print("remove    - remove a product from the basket")
    print("leave     - close the program")
    print()


def view_product_list(my_list):
    print("*** AVAILABLE PRODUCTS ***")
    print("Product \tCode \tPrice \tDescription")
    # loop to display all elements of the list



def view_basket(my_list):
    # Check if the basket is empty


    # if not empty display items in basket
 
        # print header 

        # Print list

    print()


def add_to_basket(products, basket):
    # ask user for product to be added to basket
    number = int(input("Enter the product number to add: "))
    # Check if input is valid


    # add item if the input is valid




def remove_from_basket(myBasket):
    # ask user for product to be removed from basket
    number = int(input("Enter the item number to remove: "))
    
    # Check if input is valid


    # remove item if the input is valid


    print()

def main():
    print("Product Item Program: OOP")
    print()

    # Call the FileIO read method
    productStock = []

    # Create a basket object
    basket = []

    display_menu()
    while True:
        command = input("Enter Option Choice: ")
        if command == "products":
            view_product_list(productStock)
        elif command == "basket":
            view_basket(basket)
        elif command == "add":
            add_to_basket(productStock, basket)
        elif command == "remove":
            remove_from_basket(basket)
        elif command == "leave":
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()
    print("Bye!")


if __name__ == "__main__":
    main()