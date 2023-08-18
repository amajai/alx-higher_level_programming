#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_num = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    if len(roman_string) >= 2:
        pos = -2
    else:
        pos = -1
    sum = 0
    while roman_string:
        get_roman_num = roman_num.get(roman_string[pos:])
        if get_roman_num:
            sum += get_roman_num
            roman_string = roman_string[:pos]
            pos = -2
        else:
            pos += 1
            if (pos > -1):
                break
    return sum
