from kivy.core.window import Window
from kivy.app import App
from Field import Field
from kivy.vector import Vector
from OVector import OVector


class MyApp(App):

    def build(self):
        Window.size = (600, 600)
        field = Field(shift=Vector(300, 300), stretch=Vector(60, 60))

        def g(x):
            return x ** 2

        field.add_field(g, Vector(-5, -5), Vector(5, 5), 0.5)

        field.draw()

        return field


MyApp().run()
