from math import sin, cos
class SF3:
    def phi1(self, x, y):
        return 0.3-0.1*x**2-0.2*y**2
    def phi2(self, x, y):
        return -0.2*x**2-0.1*x*y+0.7
    def f(self, x,y):
        return 0.1*x**2+x+0.2*y**2-0.3
    def g(self, x, y):
        return 0.2*x**2+y+0.1*x*y-0.7
    def dxphi1(self, x, y):
        return -0.2*x
    def dyphi1(self, x, y):
        return -0.4*y
    def dxphi2(self, x, y):
        return -0.4*x-0.1*y
    def dyphi2(self, x, y):
        return -0.1*x