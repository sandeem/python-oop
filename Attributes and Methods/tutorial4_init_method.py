class Employee:

    def __init__(self, name):
        self.name = name
          
# cannot call second method (displayEmployeeDetails) without  
# initializing the first method, hence init method is the 
# first method that is called after object as soon as object
# has been initialized       
    def displayEmployeeDetails(self):
        print(self.name)
        
employee = Employee("Mark")
employeeTwo = Employee("Mattew")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()