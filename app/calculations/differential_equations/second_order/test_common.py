from app.calculations.differential_equations.second_order.common import (
    SecondOrderDifferentialEquationSolver,
    SecondOrderDifferentialEquation,
)


def test_euler_runge_kutta_equal():
    solver = SecondOrderDifferentialEquationSolver()
    higher_order_differential_equation = SecondOrderDifferentialEquation(1, 1.5, 0.77, -0.44)
    xs1, ys1, zs1 = solver.euler(higher_order_differential_equation)
    xs2, ys2, zs2 = solver.runge_kutta(higher_order_differential_equation)
    assert abs(xs1[-1] - xs2[-1]) < 0.01
    assert abs(ys1[-1] - ys2[-1]) < 0.01
    assert abs(zs1[-1] - zs2[-1]) < 0.01
