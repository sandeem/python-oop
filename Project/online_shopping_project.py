# Simulate a online clothing account system
# Ask the user if they want to create a new account or access an existing account 
# If the user wanted to create an account, a 3 digit random number was assigned to the account
# The online system will list the items and the corresponding price when requested
# If user wants to access an existing account, accept the name and account number to validate the user 
# The existing account will display the current bill if requested


# in order to use ABCmeta and abstract method decorator (@abstractmethod) import them from module abc

from abc import ABCMeta, abstractmethod
from random import randint

# Create an abstract class called Account by making use of the metaclass
# A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves 
# ShoppingAccount class inherits from abstract base class which will make use of all these methods
# A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods and properties are overridden
# Overriding is the property of a class to change the implementation of a method provided by one of its base classes
class Account(metaclass = ABCMeta):
    @abstractmethod
    def shoppingAccounts():
        return 0
    @abstractmethod
    def customerOrderBill():
        return 0    
    @abstractmethod
    def checkExistingUser():      
        return 0
    @abstractmethod
    def displayPrice():
        return 0
    @abstractmethod
    def orderReceipt():
        return 0
    @abstractmethod
    def newestOnlineOrder():
        return 0
    @abstractmethod
    def removeExistingItems():
        return 0
    @abstractmethod
    def displayReceipt():
        return 0

# ShoppingAccount class provides layers of abstraction to the user
# The methods defined in this class will encapsulate the layers of abstraction    
# By making use of polymorphic property of overriding all these methods are overridden in our derived class
class ShoppingAccount(Account):
    # create an self parameter to access attributes of this class
    def __init__(self):
        # a empty dictionary created to store user account details 
        self.userAccount = {}
        # a dictionary to map the type of item and cost
        self.itemCost = {'Shirt': 30, 'Shoes': 40, 'Jeans': 50} 
    
    # method to create a new account     
    def shoppingAccounts(self, name):
        # to generate a random number for the user account
        self.accountNumber = randint(100, 999)
        # map the newly generated account number to the user account dictionary 
        self.userAccount.setdefault(self.accountNumber, []).append(name)
        print("Your shopping account has been created successfully. Here is your shopping account number: ", self.accountNumber)
    
    # method to add customer order to existing user account    
    def customerOrderBill(self, customerOrder):
        self.userAccount.setdefault(self.accountNumber, []).append(customerOrder)  
    
    # method to validate the existing user account  
    def checkExistingUser(self, name, accountNumber):
        if accountNumber in self.userAccount.keys():
            if self.userAccount[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            print()
            return False
    
    # method to display cost of each item
    def displayPrice(self):
        print("Cost of each item: ")
        print("Shirt: $",self.itemCost['Shirt'])
        print("Shoes: $", self.itemCost['Shoes'])
        print("Jeans: $", self.itemCost['Jeans'])

    # method to return cost of items based on user selection and quantity 
    def orderReceipt(self, item, quantity):
        return self.itemCost[item] * quantity
    
    # method to add new items     
    def newestOnlineOrder(self, newOnlineOrder):
        self.userAccount[self.accountNumber][1] += newOnlineOrder
        self.displayReceipt()
    
    # method to remove existing items    
    def removeExistingItems(self, removeItems):
        if removeItems > self.userAccount[self.accountNumber][1]:
            print("Invalid entry")
        else:
            self.userAccount[self.accountNumber][1] -= removeItems
            self.displayReceipt()
    
    # method to display current bill of the user        
    def displayReceipt(self):
        print("Current bill: $",self.userAccount[self.accountNumber][1])   

# instantiate an object for our ShoppingAccount class         
shoppingAccount = ShoppingAccount()
while True:
    # display the different options to the user
    print("Enter 1 to create a new online shopping account")
    print("Enter 2 to access an existing shopping account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = str(input())
        # pass the name to the shoppingAccounts method
        shoppingAccount.shoppingAccounts(name)
    elif userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        # pass the name and accountNumber to the checkExistingUser method
        authenticationStatus = shoppingAccount.checkExistingUser(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to display the price of each item")
                print("Enter 2 to select item")
                print("Enter 3 to show current bill")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    shoppingAccount.displayPrice()
                elif userChoice is 2:
                    print("Enter the item you want to buy")
                    item = input()
                    print("Enter the quantity of items you want to buy")
                    quantity = int(input())
                    onlineOrder = shoppingAccount.orderReceipt(item, quantity)
                    shoppingAccount.customerOrderBill(onlineOrder)
                    shoppingAccount.displayReceipt()
                    while True:
                        addOrRemove = input("Do you want to add or remove items? Type add or remove or exit\n")
                        # to add new items to the existing user account
                        if addOrRemove == 'add' or addOrRemove == 'Add' or addOrRemove == 'ADD':
                            print("Enter the item you want to buy")
                            item2 = input()
                            print("Enter the quantity of items you want to buy")
                            quantity2 = int(input())
                            newOnlineOrder = shoppingAccount.orderReceipt(item2, quantity2)
                            shoppingAccount.newestOnlineOrder(newOnlineOrder)
                        # to remove items from the existing user account
                        elif addOrRemove == 'remove' or addOrRemove == 'Remove' or addOrRemove == 'REMOVE': 
                            print("Enter the item you want to buy")
                            item2 = input()
                            print("Enter the quantity of items you want to buy")
                            quantity2 = int(input())
                            removeItems = shoppingAccount.orderReceipt(item2, quantity2)
                            shoppingAccount.removeExistingItems(removeItems)
                        else:
                            print("Thank you for shopping")
                            break
                elif userChoice is 3:
                    shoppingAccount.displayReceipt()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
