
class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOFWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. It is made of {} and it can play {} keys.".format(self.numberOfStrings,
                                                                                                     self.typeOFWood,
                                                                                                     self.numberOfMajorKeys))

guitar = Guitar()