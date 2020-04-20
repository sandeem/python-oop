'''
Created on Apr 18, 2020

@author: blizz
'''
# check if an employee has achieved his weekly target or not
class Employee:
    name = "Ben" #attribute
    designation = "Sales Executive" #attribute
    salesMadeThisWeek = 6 #attribute
    def hasAchievedTarget(self): #method
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")
            
# In order to access methods and attributes for your class, use objects to access them
# See below to create an object for the class
employeeOne = Employee() #object
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())

