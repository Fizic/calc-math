from app.calculations.differential_equations.second_order.common import (
    SecondOrderDifferentialEquation,
    SecondOrderDifferentialEquationSolver,
)
from app.export.charts.charts import create_chart
from app.export.excel.differential_equations.excel_exporter import DifferentialEquationsExcelExporter


class SecondOrderDifferentialEquationsCmd:
    """
    ДУ
    """

    def __init__(self, x_begin: float, x_end: float, y_begin: float, z_begin: float = None, **kwargs):
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.z_begin = z_begin

        self.type_of_calculations = 'du'
        self.method = ''

    def __start(self):
        super().__init__()
        self._de = SecondOrderDifferentialEquation(self.x_begin, self.x_end, self.y_begin, self.z_begin)
        self._sodes = SecondOrderDifferentialEquationSolver()

    def _finish(self, xs, ys, zs):
        deee = DifferentialEquationsExcelExporter()
        deee.create_columns(3, x_begin=self.x_begin, x_end=self.x_end, y_begin=self.y_begin, z_begin=self.z_begin)

        print("Ответ: ")
        print("x\ty\tz")
        for x, y, z in zip(xs, ys, zs):
            x, y, z = map(lambda e: round(e, 2), [x, y, z])
            print(x, y, z, sep="\t")
            deee.add_line(x, y, z)

        deee.save()
        create_chart(xs, zs)

    def euler(self):
        self.__start()
        xs, ys, zs = self._sodes.euler(self._de)
        self._finish(xs, ys, zs)

    def runge_kutta(self):
        self.__start()
        xs, ys, zs = self._sodes.runge_kutta(self._de)
        self._finish(xs, ys, zs)
