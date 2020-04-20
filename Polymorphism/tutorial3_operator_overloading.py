class Square:
    def __init__(self, side):
        self.side = side
# defined a special method __add__ to add the perimeter side lengths
# of all 4 sides for both squares        
    def __add__(squareOne, squareTwo):
        return((4*squareOne.side) + (4*squareTwo.side))

squareOne = Square(5) # 5*4 = 20
squareTwo = Square(10) # 10*4 = 40
print("Sum of both the squares = ", squareOne + squareTwo)