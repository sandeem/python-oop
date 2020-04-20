# base class
class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"
    
    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)
        
# derived class
class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017
        
    def manufactureDetails(self):
        print("This Macbook was manufactured in the year {} by {}".format(self.yearOfManufacture,self.manufacturer))

macBook = Macbook()
macBook.manufactureDetails()
macBook.contactDetails()