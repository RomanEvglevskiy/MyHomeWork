import math


def read_input():
    in_str = input().split()
    a = in_str[0]
    b = in_str[1]
    c = in_str[2]
    return int(a), int(b), int(c)


def discrim(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корней нет')
    elif d == 0:
        x = -b / (2 * a)
        print(int(round(x, 2)))
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(int(round(x1, 2)), int(round(x2, 2)))


a, b, c = read_input()
discrim(a, b, c)

if __name__ == "__main__":
    read_input()
