class Point:
    definition: str = "Abstract unit that represents a location in space"

    def __init__(self, given_x: float = 0, given_y: float = 0):
        self.x: float = given_x
        self.y: float = given_y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        return (((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)) ** 0.5

    def compute_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

class Rectangle:
    def __init__(self, method: int, *args):
        if method == 1:
            # Bottom-left corner Point
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
            # Center point
            self.center = args[0]
            self.width = args[1]
            self.height = args[2]

        elif method == 3:
            # Opposite corners
            point1 = args[0]
            point2 = args[1]
            self.center = Point(
                given_x=(point1.x + point2.x) / 2,
                given_y=(point1.y + point2.y) / 2
            )
            self.width = abs(point2.x - point1.x)
            self.height = abs(point2.y - point1.y)

        elif method == 4:
            # Four lines defining the rectangle
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
