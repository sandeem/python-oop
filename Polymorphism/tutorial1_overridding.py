class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
        
    def dislayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

# to reset the number of working from 45 to 40,
# use super() function to do it    
    def resetNumberOfWorkingHours(self):
         super().setNumberOfWorkingHours()  
        
employee = Employee()
employee.setNumberOfWorkingHours()
# using (end = ' ') at the end of print statement will let the 
# employee.dislayNumberOfWorkingHours() answer to print on the same line 
print("Number of working hours of employee: ", end = ' ')
employee.dislayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ')
trainee.dislayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ", end = ' ')
trainee.dislayNumberOfWorkingHours()