
# This program will display 12 months of sales data, calculate the total yearly sales and
# average monthly sales. Then it allows the user to edit the sales for any month. 
# This program adds IO functionality, importing the monthly_sales csv file.

import csv

FILENAME = "monthly_sales.csv"

def write_sales(sales_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)
        print("The ", FILENAME, "file was updated.")

def read_sales():
    sales_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales_list.append(row)
    return sales_list
    print("The sales list was updated.")

def display_menu():
    print("COMMAND MENU")
    print("------------")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")
    print()

def view_monthly_sales(sales_list):
    for row in sales_list:
        print(row[0] + " - " + row[1])

def view_yearly_sales(sales_list):
    total = 0
    for row in sales_list:
        total += int(row[1])
        
    print("Yearly total:\t" + str(total))
    average = round(total/ len(sales_list),2)
    print("Monthly average:\t", average)
    print()

def edit_sales(sales_list):
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # input month code
    month_code = input("Three-letter Month:\t")
    
    # month code validation
    if month_code not in months:
        print("You did not enter a valid three-letter abbreviation.")
        print()
        month_code = input("Three-letter Month:\t")
    
    # input sales value
    sales_value = input("Sales Amount:\t")
    
    # create new list
    edit_list = (month_code,sales_value)
    
    for monthly_sale, sale in enumerate(sales_list):
        if sale[0] == month_code:
            sales_list[monthly_sale] = [edit_list[0],edit_list[1]]
            write_sales(sales_list)
            print(f"Sales amount for {month_code} was modified.")
            print()

def main():
    print("Monthly Sales Program")
    print()
    display_menu()
    sales_list = read_sales()
    
    while True:
        command = input("Command:\t")
        print()
        
        if command == "monthly":
            view_monthly_sales(sales_list)
            print()
        elif command == "yearly":
            view_yearly_sales(sales_list)
        elif command == "edit":
            edit_sales(sales_list)
        elif command == "exit":
            break
        else:
            print("Not a valid option. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()