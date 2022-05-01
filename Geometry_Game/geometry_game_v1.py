from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if rect.point1.x < self.x < rect.point2.x \
                and rect.point1.y < self.y < rect.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)  # Move 100 pixels
        canvas.left(90)  # Turn 90 degrees left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()


gui_rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400))
)

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)


# rectangle = Rectangle(
#     Point(randint(0, 400), randint(0, 400)),
#     Point(randint(10, 400), randint(10, 400))
# )
# print(
#     "Rectangle coordinates is: ",
#     rectangle.point1.x, ",",
#     rectangle.point1.y, "and",
#     rectangle.point2.x, ",",
#     rectangle.point2.y
#
# )
# user_point = Point(
#     float(input("Enter 'x' value: ")),
#     float(input("Enter 'y' value: "))
# )
#
# user_area = float(input("Guess rectangle area: "))
#
# print(
#     "Your point was inside rectangle: ",
#     user_point.falls_in_rectangle(rectangle)
# )
#
# print(
#     "Your area was off by: ",
#     rectangle.area() - user_area
# )
