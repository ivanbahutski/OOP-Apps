from Math_Painter.canvas import Canvas
from Math_Painter.shapes import Square, Rectangle

canv_w = int(input("Enter canvas width: "))
canv_h = int(input("Enter canvas height: "))

colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canv_c = input("Enter canvas color (white or black): ")

canv = Canvas(canv_w, canv_h, colors[canv_c])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit. ")
    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green: "))
        blue = int(input("How much blue: "))

        square = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        square.draw(canv)

    if shape_type.lower() == 'rectangle':
        sqr_x = int(input("Enter x of the rectangle: "))
        sqr_y = int(input("Enter y of the rectangle: "))
        sqr_wdth = int(input("Enter the width length of the rectangle: "))
        sqr_hght = int(input("Enter the height length of the rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green: "))
        blue = int(input("How much blue: "))

        rect = Rectangle(sqr_x, sqr_y, sqr_wdth, sqr_hght, (red, green, blue))
        rect.draw(canv)
    if shape_type.lower() == 'quit':
        break

canv.make('canvas.png')
