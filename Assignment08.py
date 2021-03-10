# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# HClayton,7Mar21, added most needed code. Left off w/ editing 'show data'
#               section of main. Keeps repeatedly adding two values already on list?
#               Likely bc reading from file to save to list?
#           9Mar21, finished code
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
gFile_Name = 'products.txt'
gData_Table = []
gUser_Choice = ''

class Product(object):
    """Stores data about a product:

    properties:
        p_name: (string) with the products'  name
        p_price: (float) with the products' standard price
    methods:
        to_string: returns obj as string
        __doc__: defines object doc string
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <HClayton>,<07Mar21>, added 'add_data' module
    """
# -- Constructor --
    def __init__(self, p_name: str, p_price: float):
        # -- Attributes --
        try:
            self.__p_name = str(p_name)
            self.__p_price = float(p_price)
        except Exception as e:
            raise Exception('Error setting values, ensure proper format.\n' + str(e))

    # -- Properties --
    @property
    def p_name(self):
        return str(self.__p_name)

    @p_name.setter
    def p_name(self, new_name: str):
        if not str(new_name).isnumeric():
            self.__p_name = str(new_name)
        else:
            raise Exception('Names cannot be numbers')

    @property
    def p_price(self):
        return float(self.__p_price)

    @p_price.setter
    def p_price(self, new_price: float):
        if str(new_price).isnumeric():
            self.__p_price = float(new_price)
        else:
            raise Exception("Please only input numbers. EX: 30")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.p_name + ',' + str(self.p_price)


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data(file_name, data_table): saves data from a list to a file
        read_data(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <HClayton>,<07Mar21>, added save_data and read_data methods
    """

    @staticmethod
    def save_data(file_name: str, data_table: list):
        """ Saves data from dictionary into a file
           :param file_name: (string) with name of file: (gFile_Name global)
           :param data_table: (list) you want filled with file data: (gData_Table global)
           """
        file = open(file_name, 'w')
        for product in data_table:
            file.write(product.__str__() + '\n')
        file.close()

    @staticmethod
    def read_data(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file: (gFile_Name, gData_Table globals)
        :return: data_table list
        """
        data_table = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.split(',')
                    row = Product(data[0], float(data[1]))
                    data_table.append(row)
                file.close()
        except Exception as e:
            print('General Error')
            print(e, e.__doc__, type(e), sep= '\n')
        return data_table

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input/output tasks:

    methods:
        print_menu(): displays main menu
        get_user_choice(): gets user's choice, Output: user choice
        show_data(gData_Table/data_table): displays current data to user. Input: gData_Table (global data table variable), Output: None
        get_data(): captures user data input. Output: p_name, p_price
        cont_msg(''): pause program, display message
        yes_no(message): captures user input for program nav, output: str

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <HClayton>,<7Mar21>, added modules
    """
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new data
        2) View current data
        3) Save Data to File 
        4) Exit       
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def get_user_choice():
        """ Gets the menu choice from a user

        :return: user_choice
        """
        user_choice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()  # Add an extra line for looks
        return user_choice

    @staticmethod
    def show_data(data_table: list):
        """ Shows the current Tasks in the list of dictionaries rows

        :param data_table: (list) of rows you want to display, Global = gData_Table
        :return: nothing
        """
        try:
            print("******* The current product data are: *******")
            for row in data_table:
                print(str(row.p_name) + " (" + str(row.p_price) + ")")
            print("*******************************************")
            print()
        except AttributeError as e:
            print('*Incorrect data type, unreadable*' + '\n' + str(e))

    @staticmethod
    def get_data():
        """ Shows the current objects in the data list
            :return: Product object (p)
        """
        try:
            name = str(input('Enter a product name: ').strip())
            price = float(input('Enter a standard product price: ').strip())
            print('User input captured')
            p = Product(p_name=name, p_price=price)
            return p
        except Exception as e:
            print('Invalid Entry: ' + str(e))

    @staticmethod
    def cont_msg(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def yes_no(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        y_n = str(input(message)).strip().lower()
        return y_n

# Main Body of Script  ---------------------------------------------------- #
try:
    gData_Table = FileProcessor.read_data(gFile_Name)

    while True:
        IO.print_menu()
        gUser_Choice = IO.get_user_choice()

        if gUser_Choice.strip() == '1':
            gData_Table.append(IO.get_data())
            continue

        elif gUser_Choice.strip() == '2':
            IO.show_data(gData_Table)
            IO.cont_msg()
            continue

        elif gUser_Choice.strip() == '3':
            gYes_No = IO.yes_no("Save this data to file? (y/n) - ")
            if gYes_No.lower() == "y":
                FileProcessor.save_data(gFile_Name, gData_Table)
                IO.cont_msg()
                continue
            else:
                IO.cont_msg("Save Cancelled!")
                continue

        elif gUser_Choice.strip() == '4':
            gYes_No = IO.yes_no('Would you like to exit the program now? (y/n)')
            if gYes_No.lower() == 'y':
                break
            elif gYes_No.lower == 'n':
                continue
        else:
            print('Invalid menu choice, try again')
            continue

except Exception as e:
    print('Error')
    print(e, e.__doc__, type(e), sep='\n')



