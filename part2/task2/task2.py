class Rational:
    divider = 1

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def fractional_format(self):
        self.count_divider()

        fractionated_a = self.a // self.divider
        fractionated_b = self.b // self.divider

        return str(fractionated_a) + "/" + str(fractionated_b)

    def floating_point_format(self):
        quotient = self.a/self.b
        return f"{quotient:.2}"

    def count_divider(self):
        self.divider = self.find_GCD(self.a, self.b)

    def find_GCD(self, a, b):
        temp = 1

        if a < 0:
            a *= 1
        elif b < 0:
            b *= -1

        while b > 0:
            temp = b
            b = a % temp
            a = temp

        return temp