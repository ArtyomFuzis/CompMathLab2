from dataclasses import dataclass
@dataclass
class Response:
    type: str
    msg: str = None
    res: float = None
    fres: float = None
    iter_cnt: int = None
    graph: str = None
    err_1: float = None
    err_2: float = None
    res2: float = None
    delta_1: float = None
    delta_2: float = None

    def to_dict(self):
        return {'type':self.type,
                'msg':self.msg,
                'res': self.res,
                'fres': self.fres,
                'iter_cnt': self.iter_cnt,
                'graph': self.graph,
                'err_1': self.err_1,
                'err_2': self.err_2,
                'res2': self.res2,
                'delta_1': self.delta_1,
                'delta_2': self.delta_2,}