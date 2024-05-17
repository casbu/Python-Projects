import locale as lc


# Product Class that does not have set methods.
class Product:
    def __init__(self, code="", description="", price=0):
        self.__code = code
        self.__description = description
        self.__price = price

    def getCode(self):
        return self.__code

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getFormattedPrice(self):
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")

        return lc.currency(self.__price, grouping=True)

    def __str__(self):
        return self.getCode() + "; " + self.getDescription() + "; " \
               + str(self.getPrice())


class ProductInventory:
    def __init__(self):
        # Create an empty, private, productList attribute
        pass

    def addProduct(self, myProduct):
        # Append a product object to the product list attribute
        pass

    def getProduct(self, index = 0):
        # return a product based on an index parameter (default is zero)
        pass

    def getProductCount(self):
        #return the length of the product list
        pass

    # create an __iter__ and __next__ method.
    def __iter__(self):
        pass

    def __next__(self):
        pass


class Basket:
    
    def __init__(self):
        # Create an empty, private, items attribute
        pass

    def addItem(self, item):
        # Append a product object to the basket list attribute
        pass

    def removeItem(self, index=0):
        # Remove an item from the basket list attribute
        pass

    def getItemCount(self):
        #return the length of the basket list
        pass

    # create an __iter__ and __next__ method.
    def __iter__(self):
        pass

    def __next__(self):
        pass


