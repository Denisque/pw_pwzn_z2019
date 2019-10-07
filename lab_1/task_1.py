def task_11():
    for i in range(10):
        if i == 1:
            print("'''")
            print("1")
        elif i == 2:
            print("22")
        elif i == 3:
            print("333")
        elif i == 4:
            print("4444")
        elif i == 5:
            print("55555")
        elif i == 6:
            print("666666")
        elif i == 7:
            print("7777777")
        elif i == 8:
            print("88888888")
        elif i == 9:
            print("999999999")
            print("'''")
    return ''


def task_1():
    a = ("'''")
    b = ("1")
    c = ("22")
    d = ("333")
    e = ("4444")
    f = ("55555")
    g = ("666666")
    h = ("7777777")
    k = ("88888888")
    l = ("999999999")
    m = ("'''")
    return print(a), print(b), print(c), print(d), print(e), print(f), print(g), print(h), print(k), print(l), print(m)


assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''