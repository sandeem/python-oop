

# 'self' parameter
class Employee:
    
# employeeDetails method
    def employeeDetails(self):
        self.name = "Ben"

# if we delete the self parameter adn execute this program
# Python will throw an error that you have passed one parameter
# but then while receiving it you have not received it.       
# This can be overcome by using a decorator called @staticmethod
   
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")
        
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()