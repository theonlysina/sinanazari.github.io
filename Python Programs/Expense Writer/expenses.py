'''
This Python exam will involve implementing a system for managing expenses.  You will
download the skeleton of the program, then implement the functions.  The design of the
program has been set up for you.

In this system, users will be able to add and deduct expenses, update expenses, sort expenses,
and export filtered expenses to a file.  The program will initially load a collection of
expenses from a .txt file and store them in a dictionary.
'''


def import_expenses(file):
    '''Reads data from a given file and stores the expenses
    in a dictionary, where the expense type is the key
    and the total expense amount for that expense is
    the value.

    The same expense type may appear multiple times in the file.
    Ignores expenses with missing or invalid amounts.
    '''

    # create empty dict
    expenses = {}

    # open file in read mode
    with open(file, "r") as fin:

        # get all lines from file as list
        lines = fin.readlines()

        # print(lines)

        for line in lines: # iterate through lines

            if ":" in line: # find an expense
                # split expense type from expense amount
                expense_entry = line.split(":")
                expense_type = expense_entry[0]
                expense_amount_str = expense_entry[1]

                # strip whitespace from expense type and expense amount
                expense_type = expense_type.strip()
                expense_amount_str = expense_amount_str.strip()

                # check1: checks to see if expense amount can be converted to number
                if (float_convertible(expense_amount_str)):
                    # if yes, store expense amount as float
                    expense_amount = float(expense_amount_str)

                    # check 2: checks to see if expense amount in a line is positive
                    if expense_amount > 0:

                        # leftover code
                        # expense = {expense_type: expense_amount}

                        # adds expense to dictionary
                        if expenses.get(expense_type) is not None:
                            # if expense exists, adds the expense amount to previous amount
                            expenses[expense_type] += expense_amount
                        else:
                            # expense does not exist, adds expense as a new key:val item in dict
                            expenses[expense_type] = expense_amount
                    else:
                        continue
                else:
                    continue

    # print(expenses)

    return expenses

def float_convertible(value):
    """ Returns true if a value (e.g. string) is convertible to float. Returns false otherwise."""

    # attempts to convert value to float
    try:
        # if convertible to float, returns True
        float(value)
        return True

    # if not convertible to float, returns False
    except:
        return False

def is_positive(value):
    """ Returns true if a value (e.g. string) is convertible to float. Returns false otherwise."""

    # returns true if a value is positive
    if value > 0:
        return True

    # returns false otherwise
    else:
        return False

def get_expense(expenses, expense_type):
    '''Returns the value for the given expense type in the given expenses dictionary.
    Prints a friendly message and returns None if the expense type doesn't exist.
    '''

    # gets the expense amount for specified expense type
    expense_amount = expenses.get(expense_type)

    # if expense not found, notifies user with a message
    if expense_amount is None:
        print("This expense was not found. Please try another expense.")

    # returns expense amount
    return expense_amount

def add_expense(expenses, expense_type, value):
    '''Adds the given expense type and value to the given expenses dictionary.
    If the expense type already exists, adds the value to the total amount.
    Otherwise, creates a new expense type with the value.
    Prints the expense.'''

    # checks to see if value entered by user is a number
    if float_convertible(value):
        # checks to see if the value entered by user is positive
        if is_positive(value):
            # checks to see if the expense type exists
            if expenses.get(expense_type) is not None:
                # if entry passes all tests, adds value to expense type
                expenses[expense_type] += value
            else:
                # if expense type does not exist, creates a new key:val item
                expenses[expense_type] = value
        else:
            print("Please enter a positive number")
    else:
        print("Please enter a positive numeric value")

    # prints updated expense amount
    expense_amount = str(expenses.get(expense_type))
    print("Expense type of " + str(expense_type) + " is now: $" + str(expense_amount))

def deduct_expense(expenses, expense_type, value):
    '''Deducts the given value from the given expense type in the given expenses dictionary.
    Prints a friendly message if the expense type doesn't exist.
    Raises a RuntimeError if the value is greater than the existing total of the expense type.
    Prints the expense.'''

    # checks to make sure entered expense type exists -- otherwise notifies user
    if expenses.get(expense_type) is not None:

        # checks to make sure entered value is a number -- otherwise notifies user
        if float_convertible(value):

            # checks to make sure entered value is positive -- otherwise notifies user
            if is_positive(value):

                # checks to make sure expense amount for expense
                # does not turn negative after deducting value
                if not expenses[expense_type] - value < 0:
                    # deducts value from expense amount
                    expenses[expense_type] -= value
                else:
                    # if post-deduction value is negative, raises Runtime Error
                    raise RuntimeError("You cannot reduce a larger than your current expense amount.")
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a positive numeric number")
    else:
        print("The expense you entered does not exist.")

    # prints updated expense amount
    expense_amount = str(expenses.get(expense_type))
    print("Expense type of " + str(expense_type) + " is now: $" + str(expense_amount))

def update_expense(expenses, expense_type, value):
    '''Updates the given expense type with the given value in the given expenses dictionary.
    Prints a friendly message if the expense type doesn't exist.
    Prints the expense.'''

    # checks to see if expense type already exists
    if expenses.get(expense_type) is not None:
        # if it exists, updates the value
        expenses[expense_type] = value

        # and prints the updated expense amount
        expense_amount = expenses.get(expense_type)
        print("Expense type of " + str(expense_type) + " is now: $" + str(expense_amount))

    # if expense type did not exist, notifies user
    else:
        print ("Expense does not exist.")


def sort_expenses(expenses, sorting):
    '''Converts the key:value pairs in the given expenses dictionary to
    a list of tuples and sorts based on the given sorting
    argument.

    If the sorting argument is the string ‘expense_type’,
    sorts the list of tuples based on the expense type (e.g. ‘rent’),
    otherwise, if the sorting argument is ‘amount’, sorts the list based
    on the total expense amount (e.g. 825) in descending order.
    '''

    # creates a copy of expenses
    expenses_copy = expenses.copy()

    # creates a list of expenses, to be populated
    expenses_lst = []

    # makes reference to a list of key:val pairs (expense_type : expense_amount)
    items = expenses_copy.items()

    # creates a list of tuples, each an expense (an expense_type, expense amount pair)
    # iterates through all key:val pairs (items)
    for expense_type, amount in items:
        # creates a tuple (expense_type, expense_amount)
        expense = (expense_type, amount)
        # adds tuple to a list of tuples
        expenses_lst.append(expense)

    # if user chose to sort by expense type, sorts expense list by ascending expense type
    if sorting == 'expense_type':
        expenses_lst.sort(key=lambda expense: expense[0])

    # if user chose to sort by expense amount, sorts expense list by descending expense amount
    elif sorting == 'amount':
        expenses_lst.sort(key=lambda expense: expense[1])
        expenses_lst.reverse()

    # returns expense list
    return expenses_lst

def export_expenses(expenses, expense_types, file):
    '''Exports the given expense types from the given expenses dictionary to the given file.

    Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
    and exports to a file.'''

    # creates a list representing lines (strings) to be outputed
    expenses_output = []

    # iterates through expenses
    for expense_type in expense_types:
        # makes a string of expense in format (expense type: expense amount) and moves to next line
        expense_str = expense_type + ": " + str(expenses[expense_type]) + "\n"
        # adds the string to printable output
        expenses_output.append(expense_str)

    # print(expenses_output)

    # opens a file with user-specified filename in write mode
    with open(file, "w") as fout:
        # writes output list line-by-line (which is the same as in one line!)
        fout.writelines(expenses_output)
    # and automatically closes (saves) the file

def main():

    #import expense file and store in dictionary
    expenses = import_expenses('expenses.txt')

    # for testing purposes
    # print(expenses)

    while True:

        #print welcome and options
        print('\nWelcome to the expense management system!  What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Sort expenses')
        print('5: Export expenses')
        print('0: Exit the system')

        #get user input
        option_input = input('\n')

        #try and cast to int
        try:
            option = int(option_input)

        #catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            #check options
            if (option == 1):

                #get expense type and print expense info
                expense_type = input('Expense type? ')
                print(get_expense(expenses, expense_type))

            elif (option == 2):

                #get expense type
                expense_type = input('Expense type? ')

                #get amount to add and cast to float
                amount = float(input('Amount to add? '))

                #add expense
                add_expense(expenses, expense_type, amount)

            elif (option == 3):

                #get expense type
                expense_type = input('Expense type? ')
                #get amount to deduct and cast to float
                amount = float(input('Amount to deduct? '))

                #deduct expense
                deduct_expense(expenses, expense_type, amount)

            elif (option == 4):

                #get sort type
                sort_type = input('What type of sort? (\'expense_type\' or \'amount\')')

                #sort expenses
                print(sort_expenses(expenses, sort_type))

            elif (option == 5):

                # get filename to export to
                file_name = input('Name of file to export to?')

                # get expense types to export
                expense_types = []

                while True:
                    expense_type = input("What expense type you want to export? Input N to quit:")
                    if expense_type == "N":
                        break

                    expense_types.append(expense_type)

                # export expenses
                export_expenses(expenses, expense_types, file_name)

            elif (option == 0):

                #exit expense system
                print('Good bye!')
                break

if __name__ == '__main__':
    main()
