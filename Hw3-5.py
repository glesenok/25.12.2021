number_list = input('ВВедите числа через пробел: ').split()

print('Список чисел: ', number_list)

num_list = list(map(int, number_list))
print('Списрк чисел:', num_list)
print('Сумма:', sum(num_list))
