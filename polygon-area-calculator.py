class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self): # è un metodo speciale che viene chiamato quando si desidera ottenere una rappresentazione stringa di un oggetto
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5) # ** -> 'elevato a' || ** .5 -> 'elevato a 0.5' = radice quadrata
        return diagonal
    
    def get_picture(self):
        picture = ""
        if(self.height > 50 or self.width > 50):
            return "Too big for picture."
        else:
            i = 0
            while(i < self.height):
                picture += "*" * self.width + "\n"
                i += 1
            return picture

    def get_amount_inside(self, object2):
        side1 = self.width / object2.width
        side2 = self.height / object2.height
        return int(side1 * side2)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) # set width and height at the same lenght of side

    def __repr__(self):
        return f"Square(side={self.width})" # può richiamare uno tra width e height che ritorna la lunghezza di un lato del quadrato

    def set_side(self, side):
        super().__init__(side, side)
    
    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def set_height(self, side):
        super().set_width(side)
        super().set_height(side)

# test
rect = Rectangle(10, 5)
sq = Square(9)
print(rect)
print(sq)
sq.set_side(5)
print(sq)
print(sq.get_picture())