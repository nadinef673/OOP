class circle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.answer = self.length * self.width
        return(self.answer)

    def perimeter(self):
        self.answer1 = self.length + self.width
        return(self.answer1)

objcircle = circle(0, 0)
objcircle.length = int(input("Enter Length:"))
objcircle.width = int(input("Enter Width:"))
print("Area:", objcircle.area())
print("Perimeter:", objcircle.perimeter())

class triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        self.answer2 = self.base * self.height
        return(self.answer2)

objtri = triangle(0, 0)
objtri.base = int(input("Enter Base:"))
objtri.height = int(input("Enter Height:"))
print("Area:", objtri.area)
