import matplotlib.pyplot as plt


def create_chart(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Первый график')
    plt.grid()
    plt.show()
