class Rectangle():
    def __init__ (self, width ,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"sua area é {self.height * self.width}"
    

rect = Rectangle(100 , 90)

print(rect.calculate_area())