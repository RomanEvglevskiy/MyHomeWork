n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)
x = min(my_list, key=lambda i: int(i))
y = max(my_list, key=lambda i: int(i))


def mean_number():
    mean_number = sum(my_list) / len(my_list)
    return mean_number


g = mean_number()
my_list.sort()
print(x)
print(y)
print(g)
print(my_list)
