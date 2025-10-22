# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

# Hints:

# Use def methodName(self) to define a method.

# Solution:


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print (aCircle.area())



# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

# Hints:

# Use def methodName(self) to define a method.

# Solution:

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())



# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints:

# To override a method in super class, we can define a method with the same name in the super class.

# Solution:

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())


# Please raise a RuntimeError exception.

# Hints:

# Use raise() to raise an exception.

# Solution:


raise RuntimeError('something wrong')

