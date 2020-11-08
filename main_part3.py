import math
import turtle

"""
r = k * t

a - spiral step so
a = k * 2П, k = a / 2П

L = (k / 2) * (t * sqrt(1 + t^2) + ln(t + sqrt(1 + t^2)))

x = r * cos(t)
y = r * sin(t)
"""


def count_r(t):
    return k * t


def gen_spiral():
    scale = 20000
    turtle.color('blue')
    turtle.down()
    accuracy = 10
    for t in range(math.ceil(accuracy * max_t)):
        r = count_r(-t / accuracy)
        x = r * math.cos(-t / accuracy)
        y = r * math.sin(-t / accuracy)
        turtle.goto(scale * x, scale * y)
    turtle.up()
    turtle.done()


def main():
    gen_spiral()


if __name__ == '__main__':
    a = 2 / 1000  # distance between 2 rounds
    k = a / (2 * math.pi)  # from r = k * t
    max_t = 32.6107895385266  # argmax L
    main()
