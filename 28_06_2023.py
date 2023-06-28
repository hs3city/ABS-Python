
def single_string(string, index):
    if string[index] == 'I':
        return 1
    if string[index] == 'V':
        return 5
    if string[index] == 'X':
        return 10
    if string[index] == 'L':
        return 50
    if string[index] == 'C':
        return 100
    if string[index] == 'D':
        return 500
    if string[index] == 'M':
        return 1000

def double_string(string, index):
    if string[index] + string[index + 1] == 'IV':
        return 4
    if string[index] + string[index + 1] == 'IX':
        return 9
    if string[index] + string[index + 1] == 'XL':
        return 40
    if string[index] + string[index + 1] == 'XC':
        return 90
    if string[index] + string[index + 1] == 'CD':
        return 400
    if string[index] + string[index + 1] == 'CM':
        return 900

def romanToInt(s):
    arabic_number = 0
    i = 0
    last_index = len(s) -1
    while i < len(s):
        if i != last_index:
            x = double_string(s, i)
            if x is not None:
                arabic_number += x
                i+=2
                continue
        arabic_number += single_string(s, i)
        i += 1

    print(arabic_number)
    return (arabic_number)


romanToInt('IX')
