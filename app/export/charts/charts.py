import matplotlib.pyplot as plt


def create_chart(x, y):
    plt.plot(x, y, marker='o', label="y")
    plt.legend()
    plt.xlabel('x')
    plt.grid()
    plt.show()


def create_chart_with_z(x, y, z):
    plt.plot(x, y, marker='o', label="y")
    plt.plot(x, z, marker='o', label="z")
    plt.legend()
    plt.xlabel('x')
    plt.grid()
    plt.show()
