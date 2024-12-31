data = [1, 2, 3, 4]


# approach 1 using set


def approach1():
    return True if len(data) > len(set(data)) else False


def approach2():
    data = [1, 2, 3, 4]
    for item in range(1, len(data)):
        if data[item] == data[item - 1]:
            return True
    return False


def approach3():
    from collections import Counter

    data = [1, 1, 2, 3, 4]
    return any(item for item in Counter(data).values() if item > 1)


print(approach3())
