class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area1(self):
        self.answer = self.length * self.width
        return (self.answer)

objtable = rectangle(0, 0)
objtable.length = int(input("Enter length:"))
objtable.width = int(input("Enter width:"))
print("Area:", objtable.area1())
