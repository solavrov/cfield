from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse, Color, Triangle, Rectangle
from kivy.vector import Vector
from OVector import OVector
from math import inf
from kivy.core.window import Window
import cdf
import rgb


class Field(Widget):

    def __init__(self, field_function, low_left: Vector, high_right: Vector, step, paint_accuracy=20,
                 back_color=Color(0, 0, 0, 1), **kwargs):

        super().__init__(**kwargs)

        self.field = []
        self.shift = Vector(0, 0)
        self.stretch = Vector(0, 0)

        self.draw_background(back_color)
        self.calc(field_function, low_left, high_right, step)
        self.paint(paint_accuracy)
        self.normalize(step * 0.8)

    def map_ov(self, ov: OVector):
        return OVector(self.shift + self.stretch * ov.p, self.stretch * ov.v, ov.color)

    def map_v(self, v: Vector):
        return Vector(self.shift + self.stretch * v)

    def add_vector(self, ov: OVector):
        self.field.append(ov)

    def draw_field(self):
        for ov in self.field:
            ov = self.map_ov(ov)
            e = ov.v.rotate(90).normalize()
            tri_points = tuple(ov.end()) + tuple(ov.p + 2 * e) + tuple(ov.p - 2 * e)
            tri = Triangle(points=tri_points)
            dot = Ellipse(pos=(ov.p - Vector(2, 2)), size=(5, 5))
            self.canvas.add(ov.color)
            self.canvas.add(tri)
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
                x = round(x + step, 14)
            y = round(y + step, 14)

        self.stretch = Vector(Window.size[0] / (high_right.x - low_left.x),
                              Window.size[1] / (high_right.y - low_left.y))
        self.shift = Vector(-self.stretch.x * low_left.x, -self.stretch.y * low_left.y)

    def paint(self, accuracy):
        mods = []
        for ov in self.field:
            mod = ov.len()
            if mod != inf:
                mods.append(mod)
        max_mod = max(mods)
        norm_mods = [e / max_mod for e in mods]
        cdf_nodes = cdf.get_cdf_nodes(norm_mods, accuracy)
        for ov in self.field:
            mod = ov.len()
            if mod != inf:
                try:
                    t = mod / max_mod
                except ZeroDivisionError:
                    t = 0
                u = cdf.interp(t, cdf_nodes)
                ov.color = rgb.rgb1(u)
            else:
                ov.color = Color(1, 0, 0, 1)

    def normalize(self, unit):
        for ov in self.field:
            ov.normalize(unit)

    def build(self, field_function, low_left: Vector, high_right: Vector, step, paint_accuracy=20):
        self.calc(field_function, low_left, high_right, step)
        self.paint(paint_accuracy)
        self.normalize(step * 0.8)

    def draw_background(self, color):
        self.canvas.add(color)
        self.canvas.add(Rectangle(pos=(0, 0), size=Window.size))

    def draw_path(self, low_left: Vector, high_right: Vector, color=Color(1, 1, 1, 1)):
        low_left = self.map_v(low_left)
        high_right = self.map_v(high_right)
        self.canvas.add(color)
        self.canvas.add(Line(points=(low_left, (low_left.x, high_right.y)), width=1))
        self.canvas.add(Line(points=((low_left.x, high_right.y), high_right), width=1))
        self.canvas.add(Line(points=(high_right, (high_right.x, low_left.y)), width=1))
        self.canvas.add(Line(points=((high_right.x, low_left.y), low_left), width=1))

    def draw_cross(self, center=Vector(0, 0), size=1, color=Color(0.20, 0.20, 0.20, 1)):
        x_left = self.map_v(Vector(center.x - size, center.y))
        x_right = self.map_v(Vector(center.x + size, center.y))
        y_low = self.map_v(Vector(center.x, center.y - size))
        y_high = self.map_v(Vector(center.x, center.y + size))
        self.canvas.add(color)
        self.canvas.add(Line(points=(x_left, x_right), width=5))
        self.canvas.add(Line(points=(y_low, y_high), width=5))



