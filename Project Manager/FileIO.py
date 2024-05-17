import csv
import ProductObjects


FILE_NAME = "productsInStockFile.txt"

def readFromFile():
    try:
        # Create a Product Inventory Object to hold all products in the file
        
        
        # Open the file and read each row of the file
        with open(FILE_NAME, newline="") as file:
            reader = csv.reader(file)
            i = 1
            for row in reader:
                # Create a Product object and add it to the Inventory Object 

        # Return the Inventory object
        
    except FileNotFoundError:
        return None
