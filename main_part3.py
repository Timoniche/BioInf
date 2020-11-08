import math
import turtle

"""
r = k * t

a - spiral step so
a = k * 2П, k = a / 2П

x = r * cos(t)
y = r * sin(t)
"""


def count_r(t):
    return k * t


"""
with_bin_centers flag: turtle draws bin centers after spiral is drawn
"""


def gen_spiral(with_bin_centers=True):
    scale = 20000
    # scale = 200000 # set this to see bin_centers
    turtle.color('blue')
    turtle.down()
    accuracy = 10
    for t in range(math.ceil(accuracy * max_t)):
        r = count_r(clockwise * t / accuracy)
        x = r * math.cos(clockwise * t / accuracy)
        y = r * math.sin(clockwise * t / accuracy)
        turtle.goto(scale * x, scale * y)
    if with_bin_centers:
        turtle.color('red')
        turtle.penup()
        bin_centers = map(lambda xy: (xy[0] * scale, xy[1] * scale), get_approximate_centers())
        for center in bin_centers:
            turtle.goto(center[0], center[1])
            turtle.dot()
    turtle.up()
    turtle.done()


"""
L = (k / 2) * (t * sqrt(1 + t^2) + ln(t + sqrt(1 + t^2)))
"""


def count_length(t):
    return (k / 2) * ((t * math.sqrt(1 + t ** 2)) + math.log(t + math.sqrt(1 + t ** 2)))


# wolfram can't simplify it, so far this implementation
def get_approximate_centers():
    centers = []

    length_step = max_length / bins_cnt
    next_center_length = length_step / 2
    accuracy = 100
    pred_l = 0
    pred_x = 0
    pred_y = 0
    step = 0
    for t in range(math.ceil(accuracy * max_t)):
        if step == bins_cnt:
            break
        cur_l = count_length(t / accuracy)
        r = count_r(clockwise * t / accuracy)
        x = r * math.cos(clockwise * t / accuracy)
        y = r * math.sin(clockwise * t / accuracy)
        if pred_l <= next_center_length < cur_l:
            centers.append((pred_x, pred_y))
            next_center_length += length_step
            step += 1
        pred_l = cur_l
        pred_x = x
        pred_y = y
    return centers


def count_contact_matrix():
    contact_matrix = [[0 for _ in range(bins_cnt)] for _ in range(bins_cnt)]
    return contact_matrix


def main():
    gen_spiral(with_bin_centers=False)
    # print(count_contact_matrix())
    # print(get_approximate_centers())


if __name__ == '__main__':
    a = 2 / 1000  # distance between 2 rounds
    k = a / (2 * math.pi)  # from r = k * t
    max_t = 32.6107895385266  # argmax L
    max_length = 0.17
    bins_cnt = 1000
    clockwise = -1
    main()
