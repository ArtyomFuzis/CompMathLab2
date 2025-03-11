def m3(F, start, interval_a, interval_b, precision):
    if start is None:
        return None, None, None
    max_val = 0
    x = interval_a
    while x <= interval_b:
        if abs(F.dphi(x)) > max_val:
            max_val = abs(F.dphi(x))
        x += precision / 10
    if max_val >= 1:
        return 0, None, 0
    x_k = start
    iter_cnt = 0
    while True:
        iter_cnt += 1
        x_k_n = F.phi(x_k)
        if abs(x_k - x_k_n) < precision:
            return x_k_n, F.f(x_k_n), iter_cnt
        x_k = x_k_n

