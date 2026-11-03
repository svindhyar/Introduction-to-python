class Rectangle:
    '''A class to represent a rectangle'''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        '''Returns the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Returns the perimeter of the rectangle'''
        return 2 * (self.width + self.height)
    
    def is_square(self):
        '''Returns True if the rectangle is a square, False otherwise'''
        return self.width == self.height
    
for r in [Rectangle(3, 4), Rectangle(5, 5)]:
    print(r.area(), r.perimeter(), r.is_square())