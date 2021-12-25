def my_func(arg1, arg2, arg3):
    print(f'Сумма двух аргументов равна: {arg1+arg2+arg3-min([arg1, arg2, arg3])}')


my_func(int(input('Arg1')),
        int(input('Arg2')),
        int(input('Arg3')))