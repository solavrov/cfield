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


def get_division_indices(num_of_elms, num_of_intervals):
    di = int(num_of_elms / num_of_intervals)
    i_list = [0]
    while True:
        next_i = i_list[-1] + di
        if next_i > num_of_elms - 1:
            i_list.append(num_of_elms - 1)
            break
        else:
            i_list.append(next_i)
    while len(i_list) - 1 > num_of_intervals:
        i_list.pop(len(i_list) - 2)
    return i_list


def get_cdf_nodes(data, num_of_intervals):
    data = sorted(data)
    num_of_elms = len(data)
    i_list = get_division_indices(num_of_elms, num_of_intervals)
    x_list = [data[i] for i in i_list]
    y_list = [(i + 1) / num_of_elms for i in i_list]
    return [x_list, y_list]
