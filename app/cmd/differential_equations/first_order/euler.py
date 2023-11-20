from app.calculations.differential_equations.first_order.common import DifferentialEquation
from app.calculations.differential_equations.first_order.euler import euler
from app.cmd.base import BaseCmd
from app.export.charts.charts import create_chart
from app.export.excel.differential_equations.excel_exporter import DifferentialEquationsExcelExporter


def func_der_y(x, y):
    return y * (1 - x)


class EulerCmd:
    """
    Вычисление дифференциальных уравнений методом Эйлера
    """

    def __init__(self, partitions: int = None, x_begin: int = None, x_end: int = None, y_begin: int = None, **kwargs):
        self.partitions = partitions
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin

        self.type_of_calculations = 'differential_equations_euler'
        self.method = ''

    def __start(self):
        super().__init__()
        self._differential_equations = DifferentialEquation(
            self.partitions, self.x_begin, self.x_end, self.y_begin, func_der_y
        )

    def _finish(self, xs, ys):
        deee = DifferentialEquationsExcelExporter()
        deee.create_columns(2, x_begin=self.x_begin, x_end=self.x_end, y_begin=self.y_begin, method="Метод Эйлера")

        print("Ответ: ")
        print("x\ty")
        for x, y in zip(xs, ys):
            x, y = map(lambda e: round(e, 2), [x, y])
            print(x, y, sep='\t')
            deee.add_line(x, y)

        deee.save()

    def __call__(self):
        """
        Метод Эйлера
        """
        self.__start()
        self.method = 'method_euler'
        xs, ys = euler(self._differential_equations)
        create_chart(xs, ys)
        self._finish(xs, ys)
