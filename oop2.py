class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2
circle=circle(8)
print("my circle area is",circle.area())