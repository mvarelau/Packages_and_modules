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
