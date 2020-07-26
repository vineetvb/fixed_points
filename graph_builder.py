from num2word import num2word


class EnglishNumber:

    def __init__(self, number):
        self.number = number
        self.name = num2word(number)
        self.visited = False
        self.child = None

    def FindChild(self):
        l = len(self.name)
        self.child = EnglishNumber(l)
        self.visited = True
        return self.child

    def __str__(self):
        return str(self.number)


def FindFixedPoint(k):
    e = EnglishNumber(k)
    numbers = {e.number: 0}
    while (True):
        c = e.FindChild()
        if c.number in numbers:
            break
        numbers[c.number] = 0
        e = c

    return c.number


fixed_points = set()

for n in range(999999):
    fixed_points.add(FindFixedPoint(n))

print(fixed_points)  # = {4}
# There is only one fixed point for numbers below 1 million.
