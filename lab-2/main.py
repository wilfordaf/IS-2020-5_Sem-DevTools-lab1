from solution import Solution, Point
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def f(x, y):
    return x ** 2 + 5 * y ** 2


def draw_graph(func_result, color, name):
    dots = func_result[0]
    print(f"{name.upper()} minimum found in {dots[-1]} with {func_result[1]} func calculations")


def draw_graph(func_result, color, func_name):
    dots = func_result[0]
    print(f"{func_name} minimum found in {dots[-1]} with {func_result[1]} func calculations")

    xline = [i.x for i in dots]
    yline = [i.y for i in dots]
    zline = []
    for i in range(len(xline)):
        zline.append(solution.__func__([xline[i], yline[i]]))

    ax.plot3D(xline, yline, zline, color, label=func_name)

    ax.plot3D(xline, yline, zline, color, label=func_name)


if __name__ == "__main__":
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.contour3D(X, Y, Z, cmap="binary")

    start_point = Point(-4, 5)
    solution = Solution(start_point, 10 ** -6)

    constant_learning_rate = solution.constant_learning_rate_method(0.2)
    draw_graph(constant_learning_rate, "red", "constant_learning_rate")

    step_fragmentation_method = solution.step_fragmentation_method(0.1, 0.95, 0.05)

    ax.view_init(25, 25)
    plt.legend()
    plt.show()
