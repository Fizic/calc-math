from app.calculations.elementary_function.chebyshev import ChebyshevSolver
from app.cmd.base import BaseCmd


class ChebyshevCmd(BaseCmd):
    """
    Вычисление значения функции в точке по методу Чебышева
    """
    def __init__(self, x: float = None, **kwargs):
        self.x = x

        self.type_of_calculations = 'elementary_function_chebyshev'
        self.method = ''

    def __start(self):
        super().__init__()
        self._chebyshev_solver = ChebyshevSolver(self.x)

    def exp(self):
        self.__start()
        self.method = 'chebyshev_exp'
        self.answer = self._chebyshev_solver.chebyshev_exp()
        self._finish()

    def sin(self):
        self.__start()
        self.method = 'chebyshev_sin'
        self.answer = self._chebyshev_solver.chebyshev_sin()
        self._finish()
