from kivy.core.window import Window
from kivy.app import App
from Field import Field
from kivy.vector import Vector


class Program(App):

    def build(self):

        Window.size = (600, 600)

        field = Field(shift=Vector(300, 300), stretch=Vector(60, 60))

        def g(z):
            return z ** 2 * (z - 2) * (z + 2) * (z - 2j) * (z + 2j)

        def g2(z):
            return 1 / z

        field.create(g, Vector(-5, -5), Vector(5, 5), 0.25)

        field.draw()

        return field
