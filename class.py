import turtle

class Polygon():
  def __init__(self, name, sides, sizes, thick, color="blue"):
    self.name = name
    self.sides = sides
    self.sizes = sizes
    self.thick = thick
    self.color = color

  def draw(self):
    angle = (self.sides-2)*180/self.sides
    turtle.color(self.color)
    turtle.pensize(self.thick)
    for i in range(self.sides):
      turtle.forward(self.sizes)
      turtle.right(angle)


class Square(Polygon):
  def __init__(self,sizes,thick):
    super().__init__("Square", 4, sizes, thick, color="blue")

  def draw(self):
    turtle.fillcolor("orange")
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()


square = Polygon("Square", 4, 100, 5)
# square_E will return error due to override mother class fail
# square_E = Square(sides="5")
square.draw()
square_C = Square(100,5)
square_C.draw()
turtle.done()