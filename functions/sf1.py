from math import tan, cos
class SF1:
    def phi1(self, x, y):
        return tan(x*y+0.2)-x**2+x
    def phi2(self, x, y):
        return x ** 2 + 2 * y ** 2 + y - 1
    def f(self, x,y):
        return tan(x*y+0.2)-x**2
    def g(self, x, y):
        return x ** 2 + 2 * y ** 2 - 1
    def dxphi1(self, x, y):
        return 1/cos(x*y+0.2)**2-2*x+1
    def dyphi1(self, x, y):
        return 1/cos(x*y+0.2)**2
    def dxphi2(self, x, y):
        return 2*x
    def dyphi2(self, x, y):
        return 4*y+1