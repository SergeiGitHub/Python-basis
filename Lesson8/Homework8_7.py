class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
        # return f"{self.x + other.x} {self.y + other.y}"

    def __mul__(self, other):
        return (self.x * other.x - self.y.imag * other.y.imag) + (self.y * other.x + self.x * other.y)


a = ComplexNum(3, 2j)
b = ComplexNum(4, -6j)
print(a + b)
print(a * b)
