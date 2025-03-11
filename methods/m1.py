def m1(F, _, interval_a, interval_b, precision):
    if interval_a is None or interval_b is None:
        return None, None, None
    f = F.f
    a = interval_a
    b = interval_b
    iter_cnt = 0
    lst_change = None
    while b-a >= precision:
        x = a - (b-a)*f(a)/(f(b)-f(a))
        if f(x)*f(a) > 0:
            a = x
            lst_change = True
        else:
            b = x
            lst_change = False
        iter_cnt += 1
    if lst_change:
        return a, f(a), iter_cnt
    else:
        return b, f(b), iter_cnt

