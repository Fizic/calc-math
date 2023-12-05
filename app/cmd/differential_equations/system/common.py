from app.calculations.differential_equations.system.common import (
    DifferentialEquationSystem,
    DifferentialEquationSystemSolver,
)
from app.export.charts.charts import create_chart_with_z
from app.export.excel.differential_equations.excel_exporter import DifferentialEquationsExcelExporter


class SystemOfDifferentialEquationsCmd:
    """
    ДУ
    """

    def __init__(
        self,
        x_begin: float,
        y_begin: float,
        z_begin: float = None,
        t_begin: float = None,
        t_end: float = None,
        **kwargs
    ):
        self.x_begin = x_begin
        self.y_begin = y_begin
        self.z_begin = z_begin
        self.t_begin = t_begin
        self.t_end = t_end

        self.type_of_calculations = 'du'
        self.method = ''

    def __start(self):
        super().__init__()
        self._de = DifferentialEquationSystem(self.x_begin, self.y_begin, self.z_begin, self.t_begin, self.t_end)
        self._sodes = DifferentialEquationSystemSolver()

    def _finish(self, xs, ys, zs, ts):
        deee = DifferentialEquationsExcelExporter()
        deee.create_columns(4, x_begin=self.x_begin, y_begin=self.y_begin, z_begin=self.z_begin, t_begin=self.t_begin)

        print("Ответ: ")
        print("x\ty\tz\tt")
        for x, y, z, t in zip(xs, ys, zs, ts):
            x, y, z, t = map(lambda e: round(e, 5), [x, y, z, t])
            print(x, y, z, t, sep="\t")
            deee.add_line(x, y, z, t)

        deee.save()
        create_chart_with_z(xs, ys, zs)

    def euler(self):
        self.__start()
        xs, ys, zs, ts = self._sodes.euler(self._de)
        self._finish(xs, ys, zs, ts)

    def runge_kutta(self):
        self.__start()
        xs, ys, zs, ts = self._sodes.runge_kutta(self._de)
        self._finish(xs, ys, zs, ts)
