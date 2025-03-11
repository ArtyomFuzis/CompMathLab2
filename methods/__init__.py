from methods.m1 import m1
from methods.m2 import m2
from methods.m3 import m3
from methods.sm1 import sm1
def count_roots_amount(f, interval_a, interval_b, precision):
    sign = lambda x: 1 if x > 0 else -1
    cur_sign = 0
    root_cnt = 0
    x = interval_a
    while x <= interval_b:
        signf = sign(f(x))
        if cur_sign == 0:
            cur_sign = signf
        elif cur_sign != signf:
            root_cnt += 1
            cur_sign = signf
        x+=precision/10
    return root_cnt
methods = [m1, m2, m3]
smethods = [sm1]