from task_two import read_input, calculate

a, b, sign = read_input()
print(a, sign, b, end=" = ")
result = calculate(a, b, sign)
if result is not None:
    print(result)
