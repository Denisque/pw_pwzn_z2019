def task_2():
    a = '*'
    b = '* *'
    c = '* * *'
    d = '* * * *'
    e = '* * * * *'
    return print(f"{a}\n{b}\n{c}\n{d}\n{e}\n{d}\n{c}\n{b}\n{a}")


assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''