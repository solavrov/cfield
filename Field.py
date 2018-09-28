from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse, Color
from kivy.vector import Vector
from OVector import OVector


class Field(Widget):

    def __init__(self, shift=Vector(0, 0), stretch=Vector(1, 1), color=Color(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.shift = stretch
        self.stretch = shift
        self.canvas.add(color)
        self.field = []

    def map(self, ov: OVector):
        return OVector(self.stretch + self.shift * ov.origin, self.stretch + self.shift * ov)

    def add_vector(self, ov: OVector):
        self.field.append(ov)

    def draw(self):
        for ov in self.field:
            ov = self.map(ov)
            line = Line(points=(ov.origin, ov.end()), width=1)
            dot = Ellipse(pos=(ov.origin - Vector(2, 2)), size=(5, 5))
            self.canvas.add(line)
            self.canvas.add(dot)

    def add_field(self, fun, low_left: Vector, high_right: Vector, step: float):
        y = low_left.y
        while y < high_right.y:
            x = low_left.x
            while x < high_right.x:
                z = complex(x, y)
                v = Vector(fun(z).real, fun(z).imag)
                v = v.normalize() * step
                ov = OVector(Vector(x, y), v)
                self.add_vector(ov)
                x += step
            y += step




