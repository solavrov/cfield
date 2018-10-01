from kivy.core.window import Window
from kivy.app import App
from Field import Field
from kivy.vector import Vector
from kivy.graphics import Color


class Program(App):

    def build(self):
        Window.size = (700, 700)

        field = Field(shift=Vector(350, 350), stretch=Vector(70, 70))

        def g(z):
            return z ** 2 * (z - 3) * (z + 3) * (z - 3j) * (z + 3j)

        def g2(z):
            return (z - 4) * (z + 4) * (z - 4j) * (z + 4j) * z ** -2

        def g3(z):
            return z ** 4

        field.add_path(Vector(-3, -3), Vector(3, 3))
        field.create(g3, Vector(-5, -5), Vector(5, 5), 0.25)
        field.draw()

        return field
