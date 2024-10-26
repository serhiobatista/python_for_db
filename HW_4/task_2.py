class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, lower_left: Point, upper_right: Point):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def calculate_square(self):
        return (self.upper_right.y - self.lower_left.y) * (self.upper_right.x - self.lower_left.x)

    def calculate_perimeter(self):
        return (self.upper_right.y - self.lower_left.y) * 2 + (self.upper_right.x - self.lower_left.x) * 2

    