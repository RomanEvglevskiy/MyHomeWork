def read_input():
    in_str = input().split()
    a = in_str[0]
    b = in_str[2]
    sign = in_str[1]
    return int(a), int(b), sign


def calculate(a, b, sign):
    if sign == "+":
        result = a + b
        return result
    elif sign == "-":
        result = a - b
        return result
    elif sign == "*":
        result = a * b
        return result
    elif sign == "/":
        if b == 0:
            print("На ноль делить нельзя!")
        else:
            result = a / b
            return result


if __name__ == "__main__":

    read_input()

