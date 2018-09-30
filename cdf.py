from numpy import arange


def interp(x, data):

    s = [e for e in zip(*(sorted(zip(data[0], data[1]))))]
    x_list = s[0]
    y_list = s[1]

    n = len(x_list)
    i = 0
    while x > x_list[i]:
        i += 1
        if i == n:
            break

    if i == 0:
        y = y_list[0]
    elif i == n:
        y = y_list[n - 1]
    else:
        y = y_list[i - 1] + (y_list[i] - y_list[i - 1]) / (x_list[i] - x_list[i - 1]) * (x - x_list[i - 1])

    return y


def get_nodes(data, num_of_intervals=10):

    min_x = min(data)
    max_x = max(data)
    num_of_elms = len(data)
    dx = (max_x - min_x) / num_of_intervals
    x_list = list(arange(min_x, max_x + dx, dx))

    y_list = []
    for e in x_list:
        y = sum(d <= e for d in data) / num_of_elms
        y_list.append(y)

    return [x_list, y_list]
