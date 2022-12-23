# Create a class called Rational for performing arithmetic with fractions.
# Write a program to test your class.
# Use integer variables to represent the private data of the class – the numerator and the denominator.
# Provide a __init__() method that enables an object of this class to be initialized when it’s declared.
# The __init__() should contain default parameter values in case no initializers are provided
# and should store the fraction in reduced form.
# For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator.
# Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.

import math


class Rational:
    divider = 1

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.rational = {"numerator": 1, "denominator": 1}

    def fractional_format(self):
        self.count_divider()

        self.rational["numerator"] = self.a // self.divider
        self.rational["denominator"] = self.b // self.divider

        return str(self.rational["numerator"]) + "/" + str(self.rational["denominator"])

    def floating_point_format(self):
        quotient = self.a/self.b
        return f"{quotient:.2}"

    def count_divider(self):
        self.divider = math.gcd(self.a, self.b)

