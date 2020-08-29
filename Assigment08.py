# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Myao,08.25.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
product_name = ''
product_price = ''

class Product:

    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        myao,08.25.2020,Modified code to complete assignment 8
    """

    def __init__(self):
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return self.__product_price

    def product_price(self, value):
        if(value < 0):
            raise ValueError("Sorry. The Price must be greater than 0")
            self.__product_price = value


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        myao,08.25.2020,Modified code to complete assignment 8
    """

    def save_data_to_file(file_name, list_of_product_objects):
        objP1 = Product()
        objP1.product_name = "Pencil"
        objP1.product_price = "1"
        list1 = objP1.product_name + ":" + "$" + objP1.product_price

        objP2 = Product()
        objP2.product_name = "Pen"
        objP2.product_price = "5"
        list2 = objP2.product_name + ":" + "$" + objP2.product_price

        lstOfProductObjects = list1 + '\n'+ list2+ '\n'

        f = open(strFileName, "w")
        for row in lstOfProductObjects:
            f.write(str(row))
        f.close()
        return lstOfProductObjects



    def read_data_from_file(file_name):
        lstOfProductObjects.clear()  # clear current data
        f = open(strFileName, "r")
        for row in f:
            row = str(row)
            lstOfProductObjects.append(row)
        f.close()
        return lstOfProductObjects


    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Current data
        2) Add a new Task
        3) Save Data to File        
        4) Exit Program
            ''')
        print()

    @staticmethod
    def input_new_product_and_price():
        print("Type in 'product Name' and 'Price'.")
        product_name = input("Enter a product Name: ")
        product_price = input("Enter a Price: ")
        dicRow = product_name + ':' + '$' +  product_price
        lstOfProductObjects.append(dicRow)
        print('New product name and price:')
        return product_name + ':' + '$' + product_price

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    def write_data_to_file(file_name, list_of_rows):
        objFile = open(strFileName, 'w')
        for row in lstOfProductObjects:
            objFile.write(str(row))
        objFile.close()
        return lstOfProductObjects

    def print_current_list(list_of_rows):
        print("*****The current data are: *****")
        for row in lstOfProductObjects:
            print(row)
        return  '***********************************'

# Presentation (Input/Output)  -------------------------------------------- #
FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
FileProcessor.read_data_from_file(strFileName)

# Main Body of Script  ---------------------------------------------------- #
while (True):
    IO.print_menu()# Shows menu
    strChoice = IO.input_menu_choice()

# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice

    if strChoice == '1':
        print(IO.print_current_list(lstOfProductObjects))
        continue

    elif strChoice.strip() == '2':
        print(IO.input_new_product_and_price())
        continue

    # Let user add data to the list of product objects
    elif strChoice == '3':
        IO.write_data_to_file(strFileName,lstOfProductObjects)
        print('Saved!')
        continue

    # Let user exit program
    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit

    else:
        print('Oops!  That was no valid number.  Try again...')
        continue
# Main Body of Script  ---------------------------------------------------- #

