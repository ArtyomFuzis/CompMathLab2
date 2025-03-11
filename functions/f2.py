from math import cos,sin
class F2:
    def f(self, x):
        return sin(x) + cos(x)
    def df(self, x):
        return cos(x) - sin(x)
    def phi(self, x):
        return x + sin(x) + cos(x)
    def dphi(self, x):
        return 1 + cos(x) - sin(x)