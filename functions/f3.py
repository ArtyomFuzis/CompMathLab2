from math import log
class F3:
    def f(self, x):
        return log(x) +x**2+6*x-10*x**3
    def df(self, x):
        return 1/x + 2*x +6-30*x**2
    def phi(self, x):
        return log(x) +x**2+7*x-10*x**3
    def dphi(self, x):
        return 1/x + 2*x +7-30*x**2