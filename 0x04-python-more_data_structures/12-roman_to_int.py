def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    for char in roman_string[::-1]:
        value = roman_to_int_dict[char]
        if value < previous_value:
            result -= value
        else:
            result += value
    previous_value = value

    return result

