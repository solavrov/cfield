from kivy.vector import Vector
from kivy.graphics import Color
from math import inf


class OVector:

    def __init__(self, p: Vector, v: Vector, color=Color(1, 1, 1, 1)):
        self.p = p
        self.v = v
        self.color = color

    def end(self):
        return self.p + self.v

    def len(self):
        return self.v.length()

    def normalize(self, unit):
        if self.is_inf():
            self.v = Vector(0, 0)
        else:
            self.v = self.v.normalize() * unit

    def is_inf(self):
        return self.v.x == inf or self.v.y == inf
