class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):  # умножение
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):  # целочисленное деление
        return Cell(self.cell // other.cell)

    def make_order(self, row):  # нарезание ячеек на ряды по row. Например для 5 - *****\n*****\n
        n = self.cell // row
        l = self.cell % row
        print('\n'.join("".join(str("*") for i in range(row)) for c in range(n)))
        return "".join(str("*") for i in range(l))


cell_1 = Cell(13)
cell_2 = Cell(12)
cell_3 = Cell(11)
print(cell_1 + cell_2 + cell_3)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print(cell_1.make_order(5))
