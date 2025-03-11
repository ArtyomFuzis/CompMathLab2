from math import sin, cos
class SF2:
    def phi1(self, x, y):
        return 2*x+sin(y)+0.4
    def phi2(self, x, y):
        return 3*y-cos(x+1)
    def f(self, x,y):
        return x+sin(y)+0.4
    def g(self, x, y):
        return 2*y-cos(x+1)
    def dxphi1(self, x, y):
        return 2
    def dyphi1(self, x, y):
        return cos(y)
    def dxphi2(self, x, y):
        return sin(x+1)
    def dyphi2(self, x, y):
        return 3