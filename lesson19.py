# Задание 1
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def f():
    print('Пайтон')


f()
f()
f()
f()

print(f.count)

# Задача 2
list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list = (list_[0] + list_[1] + list_[2])
new_list1 = []


def quantity(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        print('Количество значений, не кратных трём: ', len(my_list) - len(new_list1))
        return f

    return wrapper


@quantity
def new_list():
    for i in my_list:
        if i % 3 == 0:
            new_list1.append(i)
    print('Список значений, кратных трём: ', new_list1)


new_list()