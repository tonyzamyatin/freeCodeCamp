class Rectangle:
  def __init__(self, width, height):
    self.width = int(width)
    self.height = int(height)

  def __repr__(self):
    stringrepr = f"Rectangle(width={self.width}, height={self.height})"
    return stringrepr

  def set_width(self, width):
    self.width = int(width)

  def set_height(self, height):
    self.height = int(height)

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      pic = self.height * (self.width * "*" + "\n")
      return pic

  def get_amount_inside(self, shape):
    amount = int(self.width/shape.width) * int(self.height/shape.height)
    return amount

class Square(Rectangle):
  def __init__(self, side):
    self.width = int(side)
    self.height = int(side)
    super().__init__(self.width, self.height)


  def __repr__(self):
    stringrepr = f"Square(side={self.width})"
    return stringrepr


  def set_side(self, side):
    self.width = int(side)
    self.height = int(side)
  
  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  
