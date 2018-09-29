from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse, Color
from kivy.vector import Vector
from OVector import OVector
from math import inf


class Field(Widget):

    def __init__(self, shift=Vector(0, 0), stretch=Vector(1, 1), **kwargs):
        super().__init__(**kwargs)
        self.shift = stretch
        self.stretch = shift
        self.field = []

    def map_ov(self, ov: OVector):
        return OVector(self.stretch + self.shift * ov.p, self.shift * ov.v, ov.color)

    def map_v(self, v: Vector):
        return Vector(self.stretch + self.shift * v)

    def add_vector(self, ov: OVector):
        self.field.append(ov)

    def draw(self):
        for ov in self.field:
            ov = self.map_ov(ov)
            line = Line(points=(ov.p, ov.e()), width=1)
            dot = Ellipse(pos=(ov.p - Vector(2, 2)), size=(5, 5))
            self.canvas.add(ov.color)
            self.canvas.add(line)
            self.canvas.add(dot)

    def calc(self, field_function, low_left: Vector, high_right: Vector, step: float):
        y = low_left.y
        while y <= high_right.y:
            x = low_left.x
            while x <= high_right.x:
                z = complex(x, y)
                try:
                    v = Vector(field_function(z).real, field_function(z).imag)
                except ZeroDivisionError:
                    v = Vector(inf, inf)
                ov = OVector(Vector(x, y), v)
                self.add_vector(ov)
                x += step
            y += step

    def paint(self):
        mods = []
        for ov in self.field:
            mod = ov.len()
            if mod != inf:
                mods.append(mod)
        max_mod = max(mods)
        for ov in self.field:
            mod = ov.len()
            if mod != inf:
                try:
                    t = mod / max_mod
                except ZeroDivisionError:
                    t = 0
                u = t ** 0.20
                ov.color = Color(u, 3 * u * (1 - u), 1 - u, 1)
            else:
                ov.color = Color(1, 0, 0, 1)

    def normalize(self, unit):
        for ov in self.field:
            ov.normalize(unit)

    def create(self, field_function, low_left: Vector, high_right: Vector, step: float):
        self.calc(field_function, low_left, high_right, step)
        self.paint()
        self.normalize(step * 0.7)

    def add_path(self, low_left: Vector, high_right: Vector, color=Color(1, 1, 1, 1)):
        low_left = self.map_v(low_left)
        high_right = self.map_v(high_right)
        self.canvas.add(color)
        self.canvas.add(Line(points=(low_left, (low_left.x, high_right.y)), width=1))
        self.canvas.add(Line(points=((low_left.x, high_right.y), high_right), width=1))
        self.canvas.add(Line(points=(high_right, (high_right.x, low_left.y)), width=1))
        self.canvas.add(Line(points=((high_right.x, low_left.y), low_left), width=1))

