from kivy.core.window import Window
from kivy.app import App
from Field import Field
from kivy.vector import Vector
from kivy.graphics import Color
from math import cos, sin, exp


class Program(App):

    def build(self):

        Window.size = (700, 700)

        def g(z):
            return z * (z - 2j)

        def g2(z):
            return (z - 4) * (z + 4) * (z - 4j) * (z + 4j) * z ** -2

        def g3(z):
            return (z + 2) * (z - 2)

        def g4(z):
            return z ** 8 - 3 ** 8

        def expc(z: complex):
            return exp(z.real) * complex(cos(z.imag), sin(z.imag))

        def sinc(z: complex):
            j = complex(0, 1)
            return (expc(j*z) - expc(-j*z)) / (2 * j)

        def cosc(z: complex):
            j = complex(0, 1)
            return (expc(j * z) + expc(-j * z)) / 2

        def g5(z: complex):
            return sinc(1/z)

        def g6(z):
            return 1/z

        field = Field(g, Vector(-5, -5), Vector(5, 5), 0.2)
        field.draw_cross()
        field.draw_path(Vector(-4, -4), Vector(4, 4))
        field.draw_field()

        return field
