from kivy.graphics import Color


def rgb1(u):
    r = u
    g = 4 * u * (1 - u)
    b = 1 - u
    return Color(r, g, b, 1)


def rgb2(u):
    b = max(0, (1 - 2 * u))
    r = max(0, (2 * u - 1))
    g = 1 - b - r
    return Color(r, g, b, 1)
