def read_lst():
    n = int(input())
    my_list = []
    for i in range(n):
        number = int(input())
        my_list.append(number)
    print(my_list)


read_lst()


def read_string():
    a = input().split()
    l = []
    for i in range(len(a)):
        l.append(int(a[i]))
    print(l)


read_string()
