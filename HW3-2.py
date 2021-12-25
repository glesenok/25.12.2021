def data(**kwargs):
    return list(kwargs.values())


def data_1 ():
     print(data(name = input('name:'),
                lastname = input('lastname: '),
                bd = input('bd: '),
                phone = input('phone: '),
                email = input('email: '),
                city = input('city: ')))


