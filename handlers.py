from flask import make_response
from functions import funcs, sfuncs
from methods import methods, count_roots_amount, smethods
import response


def handle_equation(json: dict):
    try:
        f_id = json['func_id']
        meth_id = json['method_id']
        start = json['start']
        interval_a = json['interval_a']
        interval_b = json['interval_b']
        precision = json['precision']
        if not isinstance(f_id, int):
            return make_response('Wrong type func_id', 400)
        if not isinstance(meth_id, int):
            return make_response('Wrong type meth_id', 400)
        if not isinstance(start, float) and not start is None:
            return make_response('Wrong type start', 400)
        if not isinstance(interval_a, float) and interval_a is not None:
            return make_response('Wrong type interval_a', 400)
        if not isinstance(interval_b, float) and interval_b is not None:
            return make_response('Wrong type interval_b', 400)
        if not isinstance(precision, float):
            return make_response('Wrong type precision', 400)
        if len(funcs) < f_id or f_id <= 0:
            return make_response('Function not found', 400)
        f = funcs[f_id-1]()
        if (a := handle_roots_amount(count_roots_amount(f.f, interval_a, interval_b, precision))) is not None:
            return a
        if start is not None and interval_a is not None and interval_b is not None and not (interval_a <= start <= interval_b):
            return make_response(response.Response(type="err", msg="Начальное приближение не лежит в выбранном интервале").to_dict(), 200)
        if interval_a is not None and interval_b is not None and not (interval_a <= interval_b):
            return make_response(response.Response(type="err", msg="Левый конец интервала больше правого").to_dict(), 200)
        if len(methods) < meth_id or meth_id <= 0:
            return make_response('Method not found', 400)
        m = methods[meth_id-1]
        res, fres, iter_cnt = m(f,start, interval_a, interval_b, precision)
        if res is None:
            return make_response(response.Response(type="err", msg="Не всех обязательные поля заполнены").to_dict(), 200)
        if fres is None:
            return make_response(response.Response(type="err", msg="Метод простой итерации не будет сходится при данных значениях").to_dict(), 200)

        return make_response(response.Response(type="equation_res", res = res, fres = fres, iter_cnt=iter_cnt).to_dict(), 200)

    except KeyError:
        return make_response('Some of required fields are missing', 400)
    except ValueError:
        return make_response(response.Response(type="err", msg="Выбранный интервал не входит в область определения функции").to_dict(), 200)



def handle_roots_amount(amount):
    if amount == 0:
        return make_response(response.Response(type="err", msg="Корень не найден на выбранном отрезке").to_dict(), 200)
    if amount > 1:
        return make_response(response.Response(type="err", msg=f"Найдено следующее количество корней: {amount}, что больше, чем 1").to_dict(), 200)
    return None

def handle_system(json : dict):
    try:
        f_id = json['func_id']
        meth_id = json['method_id']
        start_x = json['start_x']
        start_y = json['start_y']
        interval_a_x = json['interval_a_x']
        interval_a_y = json['interval_a_y']
        interval_b_x = json['interval_b_x']
        interval_b_y = json['interval_b_y']
        precision = json['precision']
        if not isinstance(f_id, int):
            return make_response('Wrong type func_id', 400)
        if not isinstance(meth_id, int):
            return make_response('Wrong type meth_id', 400)
        if not isinstance(start_x, float):
            return make_response('Wrong type start_x', 400)
        if not isinstance(start_y, float):
            return make_response('Wrong type start_y', 400)
        if not isinstance(interval_a_x, float):
            return make_response('Wrong type interval_a_x', 400)
        if not isinstance(interval_a_y, float):
            return make_response('Wrong type interval_a_y', 400)
        if not isinstance(interval_b_x, float):
            return make_response('Wrong type interval_b_x', 400)
        if not isinstance(interval_b_y, float):
            return make_response('Wrong type interval_b_y', 400)
        if not isinstance(precision, float):
            return make_response('Wrong type precision', 400)
        if len(sfuncs) < f_id or f_id <= 0:
            return make_response('Function not found', 400)
        f = sfuncs[f_id-1]()
        if start_x is not None and interval_a_x is not None and interval_b_x is not None and not (interval_a_x <= start_x <= interval_b_x):
            return make_response(response.Response(type="err", msg="Начальное приближение не лежит в выбранном интервале(по x)").to_dict(), 200)
        if start_y is not None and interval_a_y is not None and interval_b_y is not None and not (interval_a_y <= start_y <= interval_b_y):
            return make_response(response.Response(type="err", msg="Начальное приближение не лежит в выбранном интервале(по y)").to_dict(), 200)
        if len(smethods) < meth_id or meth_id <= 0:
            return make_response('Method not found', 400)
        m = smethods[meth_id-1]
        res_x, res_y, iter_cnt, err_x, err_y, delta1, delta2 = m(f, start_x, start_y, interval_a_x, interval_a_y, interval_b_x, interval_b_y, precision)
        if res_x is None:
            return make_response(response.Response(type="err", msg="Метод простой итерации не будет сходится при данных значениях").to_dict(), 200)
        return make_response(response.Response(type="system_res", res = res_x, res2= res_y, iter_cnt=iter_cnt, err_1= err_x, err_2 = err_y, delta_1=delta1, delta_2=delta2).to_dict(), 200)
    except KeyError:
        return make_response('Some of required fields are missing', 400)
    except ValueError:
        return make_response(response.Response(type="err", msg="Выбранный интервал не входит в область определения функции").to_dict(), 200)

