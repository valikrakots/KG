from matplotlib import pyplot as plt
import time


def figure1():
    f = plt.figure(1, figsize=(8, 8))
    ax = f.gca()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])

    x1, y1 = 1.0, 1.0
    x2, y2 = 20.0, 40.0

    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    dx = abs(x2 - x1) / (max(abs(x2 - x1), abs(y2 - y1) * 2))

    if x2 > x1:
        dx = dx
    else:
        dx = -dx

    x = x1
    y = k * x + b

    begin = time.time()

    while x < x2:
        ax.plot(x, y, 'ko')
        f.canvas.draw()
        y = k * x + b
        x += dx

    end = time.time()
    print(f'Пошаговый алгоритм: {end - begin}')
    f.show()


def figure2():
    f = plt.figure(2, figsize=(8, 8))
    ax = f.gca()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])

    x1, y1 = 0.0, 0.0
    x2, y2 = 20.0, 40.0

    dx, dy = x2 - x1, y2 - y1

    if dx > dy:
        steps = dx
    else:
        steps = dy

    x_increment = dx / steps
    y_increment = dy / steps

    begin = time.time()
    for i in range(int(steps)):
        ax.plot(x1, y1, 'ko')
        f.canvas.draw()
        x1 += x_increment
        y1 += y_increment

    end = time.time()
    print(f'Алгоритм ЦДА: {end - begin}')
    f.show()


def figure3():
    f = plt.figure(3, figsize=(8, 8))
    ax = f.gca()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])

    x1, y1 = 0.0, 0.0
    x2, y2 = 20.0, 40.0

    dx, dy = x2 - x1, y2 - y1
    slope = abs(dy / dx)

    error = 0.0
    x, y = x1, y1

    begin = time.time()
    while x < x2:
        ax.plot(x, y, 'ko')
        f.canvas.draw()
        x += 1
        error = error + slope
        if error >= 0.5:
            y += 1
            error -= 1.0

    end = time.time()
    print(f'Алгоритм Брезенхема: {end - begin}')
    f.show()


def figure4():
    f = plt.figure(4, figsize=(8, 8))
    ax = f.gca()
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])

    r = 20
    x, y = 0, r
    d = 3 - 2 * r

    def plot(_x, _y, _radius):
        ax.plot(_x, _y, 'ko')
        ax.plot(-_x, _y, 'ko')
        ax.plot(_x, -_y, 'ko')
        ax.plot(-_x, -_y, 'ko')

        ax.plot(_y, _x, 'ko')
        ax.plot(_y, -_x, 'ko')
        ax.plot(-_y, _x, 'ko')
        ax.plot(-_y, -_x, 'ko')
        f.canvas.draw()

    begin = time.time()
    while y >= x:
        plot(x, y, r)
        x += 1
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6

    end = time.time()
    print(f'Алгоритм Брезенхема (окружность): {end - begin}')
    f.show()


def pause():
    input("Press the <ENTER> key to continue...")


if __name__ == '__main__':
    figure1()
    figure2()
    figure3()
    figure4()
    pause()
