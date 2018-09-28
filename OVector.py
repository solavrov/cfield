from kivy.vector import Vector


class OVector(Vector):

    def __init__(self, origin:  Vector, vector: Vector):
        super().__init__(vector)
        self.origin = origin

    def end(self):
        return self.origin + self
