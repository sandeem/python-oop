

# 'self' parameter
class Employee:
    
# employeeDetails method
    def employeeDetails(self):
        self.name = "Matt"
        print("Name = ", self.name)
        age = 30
        print("Age = ", age)

# printEmployeeDetails method      
    def printEmployeeDetails(self):
        print("Name = ", self.name)
        print("Age = ", age)
    
employee = Employee()
# most commonly used approach to call a class
employee.employeeDetails()
# least commonly used approach to call a class
Employee.employeeDetails(employee)

# this statement will cause an error because
# the age attribute cannot be accessed within the 
# printEmployeeDetails method for the age atribute 
# created within the employeeDetails method did not 
# use name of the object ('self'), run this program 
# to understand this
employee.printEmployeeDetails()


