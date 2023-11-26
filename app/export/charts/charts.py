import matplotlib.pyplot as plt


def create_chart(x, y, z):
    plt.plot(x, y, marker='o', label="y")
    plt.plot(x, z, marker='o', label="z")
    plt.legend()
    plt.xlabel('x')
    plt.grid()
    plt.show()
