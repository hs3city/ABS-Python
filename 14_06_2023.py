# 1. listy w listach


x = [100, 20, 30, 50, 1, -1, 99, -100]

x2 = sorted(x)
print(x2)

print(x)

result = x.sort()
print(x)

print(result)


# def sorted(lista):
#     result = []
#     ...
#     result.append(x)
#     ...
#     return result
#
# class list:
#     def sort(self):
#         ...
#

y = 100


def some_funciton(jakas_liczba):
    print(jakas_liczba)
    y = 20
    print(y)



some_funciton(y)



def change_second_element_to_A(some_list):
    some_list[1] = 'A'
    return 'abc'


list1 = [1, 2, 3, 4]
list2 = list1.append(5)

b = [1, 2, 3, 4]
x = b.append(5)
print(f'{b=}')
print(f'{x=}')
change_second_element_to_A(b)

print(b)


def get_first_negative(numbers):
    for number in numbers:
        if number < 0:
            return number
    return None

a_list = [1, 2, 3, 4, 5, -1]
some_negative = get_first_negative(a_list)

if some_negative is not None:
    print(f'negative number is {some_negative}')