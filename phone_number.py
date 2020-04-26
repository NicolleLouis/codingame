import sys

class Cell(object):
    def __init__(self, number):
        self.number = number
        self.children = []

    def has_child(self, number):
        for child in self.children:
            if child.number == number:
                return True
        return False

    def get_child(self, number):
        for child in self.children:
            if child.number == number:
                return child
        return False

    def add_child(self, child):
        self.children.append(child)


def add_phone_number_to_cell(telephone, ancestor_cell, total_cell):
    parent_cell = ancestor_cell
    for number in telephone:
        if parent_cell.has_child(int(number)):
            parent_cell = parent_cell.get_child(int(number))
            continue
        else:
            total_cell += 1
            child_cell = Cell(int(number))
            parent_cell.add_child(child_cell)
            parent_cell = child_cell
    return total_cell

ancestor_cell = Cell(int(-1))
total_cell = 0

n = int(input())
for i in range(n):
    telephone = input()
    total_cell = add_phone_number_to_cell(telephone, ancestor_cell, total_cell)
    print(total_cell, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# The number of elements (referencing a number) stored in the structure.
print(total_cell)
