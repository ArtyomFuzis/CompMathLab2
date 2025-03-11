class F4:
    def f(self, x):
        return x**10 - 4 * x ** 4 - 100 * x ** 2 + 6 * x ** 3 - 25 * x
    def df(self, x):
        return 10*x**9 - 16 * x ** 3 - 200 * x + 18 * x ** 2 - 25
    def phi(self, x):
        return x**10 - 4 * x ** 4 - 100 * x ** 2 + 6 * x ** 3 - 24 * x
    def dphi(self, x):
        return 10*x**9 - 16 * x ** 3 - 200 * x + 18 * x ** 2 - 24