class F1:
    def f(self, x):
        return 4.45*x**3+7.81*x**2-9.62*x-8.17
    def df(self, x):
        return 13.35*x**2+15.62*x-9.62
    def phi(self, x):
        return (4.45*x**3+7.81*x**2-8.17)/9.62
    def dphi(self, x):
        return (13.35*x**2+15.62*x)/9.62