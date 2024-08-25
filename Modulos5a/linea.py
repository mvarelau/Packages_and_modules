from punto import Point

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        return (((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)) ** 0.5

    def compute_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
