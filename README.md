# Packages_and_modules
repo challenge #5

```
modulos_5/
├── __init__.py
├── geometria.py
└── main.py
```

# Pachage with one module that has all the classes and functions 
## Code of the module 
```python
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
```
## Call of the module at `main.py`
```python 
from geometria import Point
from geometria import Line
from geometria import Rectangle

if __name__ == "__main__":
    method = int(input("Enter the method you want to use to create the rectangle (1, 2, 3 or 4): "))

    if method == 1:
        x = float(input("Enter the x coordinate of the bottom-left corner: "))
        y = float(input("Enter the y coordinate of the bottom-left corner: "))
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rectangle = Rectangle(1, Point(x, y), width, height)

    elif method == 2:
        x = float(input("Enter the x coordinate of the center: "))
        y = float(input("Enter the y coordinate of the center: "))
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rectangle = Rectangle(2, Point(x, y), width, height)

    elif method == 3:
        x1 = float(input("Enter the x coordinate of the first point: "))
        y1 = float(input("Enter the y coordinate of the first point: "))
        x2 = float(input("Enter the x coordinate of the second point: "))
        y2 = float(input("Enter the y coordinate of the second point: "))
        rectangle = Rectangle(3, Point(x1, y1), Point(x2, y2))

    elif method == 4:
        points = []
        for i in range(4):
            print(f"Line {i+1}:")
            start_x = float(input("Enter the x coordinate of the start point: "))
            start_y = float(input("Enter the y coordinate of the start point: "))
            end_x = float(input("Enter the x coordinate of the end point: "))
            end_y = float(input("Enter the y coordinate of the end point: "))
            points.append(Line(Point(start_x, start_y), Point(end_x, end_y)))
        rectangle = Rectangle(4, *points)
    
    print(f"Area of the rectangle: {rectangle.compute_area()}")
    print(f"Perimeter of the rectangle: {rectangle.compute_perimeter()}")

    test_x = float(input("Enter the x coordinate of the test point: "))
    test_y = float(input("Enter the y coordinate of the test point: "))
    test_point = Point(test_x, test_y)
    if rectangle.compute_interference_point(test_point):
        print("The point is inside the rectangle.")
    else:
        print("The point is outside the rectangle.")
```
# Classes in diferent modules 
```
├── Modulo5b/
│   ├── __init__.py
│   ├── punto.py
│   ├── linea.py
│   ├── rectangulo.py
│
├── main.py
```
## `punto.py`
```python
class Point:
    def __init__(self, given_x: float = 0, given_y: float = 0):
        self.x = given_x
        self.y = given_y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0
```
## `linea.py`

```python
from Modulo5a.punto import Point

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        return (((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)) ** 0.5

    def compute_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
```
 ## `rectangulo.py`

 ```python
from Modulo5a.punto import Point
from Modulo5a.linea import Line

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
```






