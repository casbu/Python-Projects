# Cass Burleson
# Jun 15, 2023
# Description: This program imports a seperate module into the main function to calculate sales tax and total after tax.

import CalculationsModule as cM

# CONST
DASHES = "-" * 20

def main():
    #print header
    print(DASHES)
    print("Sales Tax Calculator")
    print(DASHES)

    again = "y"

    # loop that checks for more input
    while again.lower() == "y":
        item = 0
        total = 0
        #prints instructions
        print("ENTER ITEMS (ENTER -99 to END)")
        
        # loop that collects user input for items and calculates the total
        while item != -99:
            total += item
            item = float(input("Cost of item:\t"))

        # calls CalculationsModule to get salesTax and totalAfterTax            
        salesTax = cM.salesTax(total)
        totalAfterTax = cM.totalAfterTax(total,salesTax)
        
        #prints output message
        print()
        print(f"Total:\t\t\t{round(total,2)}")
        print(f"Sales Tax:\t\t{salesTax}")
        print(f"Total after tax:\t{totalAfterTax}")

        # ask for new data
        print()
        again = input("Again?\t (y/n):\t")
        print(DASHES)
        print(DASHES)
        
    else:
        #end program message
        print("Thanks, bye!")
        
if __name__ == "__main__":
    main()