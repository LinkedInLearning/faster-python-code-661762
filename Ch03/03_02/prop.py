"""Properties example"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(type(value))
        self._y = value
