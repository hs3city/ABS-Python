

def romanToInt(s):
    r = list(s)
    arabic_number = []
    for i in range(len(r)):
        if i < len(r):
            if r[i] + r[i + 1] == 'IV':
                arabic_number.append(4)
                del r[i]
                del r[i + 1]
            if r[i] + r[i + 1] == 'IX':
                arabic_number.append(9)
                del r[i]
                del r[i + 1]
            if r[i] + r[i + 1] == 'XL':
                arabic_number.append(40)
                del r[i]
                del r[i + 1]
            if r[i] + r[i + 1] == 'XC':
                arabic_number.append(90)
                del r[i]
                del r[i + 1]
            if r[i] + r[i + 1] == 'CD':
                arabic_number.append(400)
                del r[i]
                del r[i + 1]
            if r[i] + r[i + 1] == 'CM':
                arabic_number.append(900)
                del r[i]
                del r[i + 1]
        if r[i] == 'I':
            arabic_number.append(1)
            del r[i]
        if r[i] == 'V':
            arabic_number.append(5)
            del r[i]
        if r[i] == 'X':
            arabic_number.append(10)
            del r[i]
        if r[i] == 'L':
            arabic_number.append(50)
            del r[i]
        if r[i] == 'C':
            arabic_number.append(100)
            del r[i]
        if r[i] == 'D':
            arabic_number.append(500)
            del r[i]
        if r[i] == 'M':
            arabic_number.append(1000)
            del r[i]
    print(sum(arabic_number))
    return (sum(arabic_number))


romanToInt('IV')
