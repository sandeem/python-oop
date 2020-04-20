class Employee:
    numberOfWorkingHours = 40
    
# Creating a class attribute
employeeOne = Employee()
employeeTwo = Employee()

print("Number of working hours for employee one is ",employeeOne.numberOfWorkingHours,".")
print("Number of working hours for employee two is ",employeeOne.numberOfWorkingHours,".")

# Changing the number of working hours for all employees

Employee.numberOfWorkingHours = 45

print("New number of working hours for employee one is ",employeeOne.numberOfWorkingHours,".")
print("New number of working hours for employee two is ",employeeOne.numberOfWorkingHours,".")

# Creating an instance attribute

employeeOne.name = "Ben"
employeeTwo.name = "John"
