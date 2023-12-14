from app.calculations.elementary_function.chebyshev import ChebyshevSolver
from app.cmd.base import BaseCmd


class ChebyshevCmd(BaseCmd):
    """
    Вычисление значения функции в точке по методу Чебышева
    func = 1 - функция exp(x)
    func = 2 - функция sin(x)
    """
    def __init__(self, x: float = None, func: float = None, **kwargs):
        self.x = x
        self.func = func

        self.type_of_calculations = 'elementary_function_chebyshev'
        self.method = ''

    def __start(self):
        super().__init__()
        self._chebyshev_solver = ChebyshevSolver(self.x, self.func)

    def __call__(self):
        self.__start()
        self.method = 'chebyshev'
        self.answer = self._chebyshev_solver.chebyshev()
        self._finish()
