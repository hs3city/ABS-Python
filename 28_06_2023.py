

def romanToInt(s):
    arabic_number = 0
    i = 0
    while i < len(s):
        if s[i] + s[i+1] == 'IV':
            arabic_number += 4
            i+=2
            continue
        if s[i] + s[i+1] == 'IX':
            arabic_number += 9
            i += 2
            continue
        if s[i] + s[i+1] == 'XL':
            arabic_number += 40
            i += 2
            continue
        if s[i] + s[i+1] == 'XC':
            arabic_number += 90
            i += 2
            continue
        if s[i] + s[i+1] == 'CD':
            arabic_number += 400
            i += 2
            continue
        if s[i] + s[i+1] == 'CM':
            arabic_number += 900
            i += 2
            continue

        if s[i] == 'I':
            arabic_number+=1
            i += 1
            continue
        if s[i] == 'V':
            arabic_number+=5
            i += 1
            continue
        if s[i] == 'X':
            arabic_number+=10
            i += 1
            continue
        if s[i] == 'L':
            arabic_number+=50
            i += 1
            continue
        if s[i] == 'C':
            arabic_number+=100
            i += 1
            continue
        if s[i] == 'D':
            arabic_number+=500
            i += 1
            continue
        if s[i] == 'M':
            arabic_number+=1000
            i += 1
            continue
    print(arabic_number)
    return (arabic_number)


romanToInt('MCMXCIV')
