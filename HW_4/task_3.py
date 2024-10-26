class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, lower_left: Point, upper_right: Point):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def calculate_square(self) -> int:
        return (self.upper_right.y - self.lower_left.y) * (self.upper_right.x - self.lower_left.x)

    def calculate_perimeter(self) -> int:
        return (self.upper_right.y - self.lower_left.y) * 2 + (self.upper_right.x - self.lower_left.x) * 2

    def contains(self, coord: Point) -> bool:
        if self.lower_left.x < coord.x < self.upper_right.x and self.lower_left.y < coord.y < self.upper_right.y:
            return True
        else:
            return False
    