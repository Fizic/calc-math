from app.calculations.differential_equations.system.common import (
    DifferentialEquationSystem,
    DifferentialEquationSystemSolver,
)


def test_system_euler_runge_kutta_equal():
    solver = DifferentialEquationSystemSolver()
    differential_equation_system = DifferentialEquationSystem(2, 1, 1, 0, 0.3)
    xs1, ys1, zs1, ts1 = solver.euler(differential_equation_system)
    xs2, ys2, zs2, ts2 = solver.runge_kutta(differential_equation_system)
    assert abs(xs1[-1] - xs2[-1]) < 0.01
    assert abs(ys1[-1] - ys2[-1]) < 0.01
    assert abs(zs1[-1] - zs2[-1]) < 0.01
    assert abs(ts1[-1] - ts2[-1]) < 0.01
