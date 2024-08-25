from punto import Point
from linea import Line

class Rectangle:
    def __init__(self, method: int, *args):
        if method == 1:
            bottom_left = args[0]
            width = args[1]
            height = args[2]
            self.center = Point(
                given_x=bottom_left.x + width / 2,
                given_y=bottom_left.y + height / 2
            )
            self.width = width
            self.height = height

        elif method == 2:
            self.center = args[0]
            self.width = args[1]
            self.height = args[2]

        elif method == 3:
            point1 = args[0]
            point2 = args[1]
            self.center = Point(
                given_x=(point1.x + point2.x) / 2,
                given_y=(point1.y + point2.y) / 2
            )
            self.width = abs(point2.x - point1.x)
            self.height = abs(point2.y - point1.y)

        elif method == 4:
            line1 = args[0]
            line3 = args[2]
            self.center = Point(
                given_x=(line1.start.x + line3.end.x) / 2,
                given_y=(line1.start.y + line3.end.y) / 2
            )
            self.width = line1.compute_length()
            self.height = line3.compute_length()

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point: Point) -> bool:
        left_x = self.center.x - self.width / 2
        right_x = self.center.x + self.width / 2
        bottom_y = self.center.y - self.height / 2
        top_y = self.center.y + self.height / 2
        return left_x <= point.x <= right_x and bottom_y <= point.y <= top_y
