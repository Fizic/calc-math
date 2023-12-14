from app.cmd.elementary_function.chebyshev import ChebyshevCmd
from app.cmd.elementary_function.iteration import IterationCmd
from app.cmd.elementary_function.rows import RowsCmd


class ElementaryFunctionCmd:
    """
    Вычисление значения элементарной функции в точке
    """

    def __init__(self, **kwargs):
        self.chebyshev = ChebyshevCmd(**kwargs)
        self.iteration = IterationCmd(**kwargs)
        self.rows = RowsCmd(**kwargs)
