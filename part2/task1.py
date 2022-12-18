# Create a class Rectangle with attributes length and width, each of which defaults to 1.
# Provide methods that calculate the perimeter and the area of the instantiation.
# Also, provide setter and getter for the length and width attributes.
# The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width

    def get_attributes(self):
        return f"length = {self.length}, width = {self.width}"

    def set_attributes(self, length, width):
        if length > 0.0 and length < 20.0 and width > 0.0 and width < 20.0:
            self.length = length
            self.width = width
        else:
            print("Length and width should be in [0.0; 20.0]")

rectangle = Rectangle()

print(rectangle.get_attributes())
rectangle.set_attributes(11.5, 12.0)

print("perimeter:", rectangle.perimeter())
print("square:", rectangle.square())
