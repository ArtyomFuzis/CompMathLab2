def sm1(SF, start_x, start_y, interval_a_x, interval_a_y, interval_b_x, interval_b_y, precision):
    cur_x = interval_a_x
    cur_y = interval_a_y
    max_val1 = 0
    max_val2 = 0
    while cur_x < interval_b_x:
        while cur_y < interval_b_y:
            cur_val1 = abs(SF.dxphi1(cur_x, cur_y)) + abs(SF.dyphi1(cur_x, cur_y))
            cur_val2 = abs(SF.dxphi2(cur_x, cur_y)) + abs(SF.dyphi2(cur_x, cur_y))
            if cur_val1 > max_val1:
                max_val1 = cur_val1
            if cur_val2 > max_val2:
                max_val2 = cur_val2
            cur_y += precision
        cur_x += precision
    if max_val1 >= 1 or  max_val2 >= 1:
        print(max_val1, max_val2)
        return None,None,None,None,None,None,None    #res_x, res_y, iter_cnt, err_x, err_y, delta_x, delta_y
    cur_x = start_x
    cur_y = start_y
    iter_cnt = 0
    while True:
        iter_cnt += 1
        nxt_x = SF.phi1(cur_x, cur_y)
        nxt_y = SF.phi2(cur_x, cur_y)
        if abs(nxt_x - cur_x) < precision and  abs(nxt_y - cur_y) < precision:
            return nxt_x, nxt_y, iter_cnt, abs(nxt_x - cur_x), abs(nxt_y - cur_y), SF.f(nxt_x, nxt_y), SF.g(nxt_x, nxt_y)
        cur_x = nxt_x
        cur_y = nxt_y
