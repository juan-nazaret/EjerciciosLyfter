class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = ((self.radius * self.radius) * 3.1416)
        return area


circle1 = Circle(8)
print(f'area: {circle1.get_area()}')