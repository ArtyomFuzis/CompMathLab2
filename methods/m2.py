def m2(F, start, _, __, precision):
    if start is None:
        return None,None,None
    x_k = start
    iter_cnt = 0
    while True:
        iter_cnt+=1
        n_x_k = x_k - F.f(x_k)/F.df(x_k)
        if abs(n_x_k-x_k) < precision:
            return n_x_k, F.f(n_x_k), iter_cnt
        x_k = n_x_k

