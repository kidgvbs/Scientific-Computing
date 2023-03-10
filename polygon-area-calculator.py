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
            for i in range (0, self.height, 1):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self):
        pass

class Square(Rectangle):
    pass


rect = Rectangle(10, 5)
print(rect.get_picture())