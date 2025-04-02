"""
Practice Problem (Mock)
"""



test_case_one = 58

def roman_numeral_creator(num: int) -> str:

    roman_numeral = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    roman_result = ""
    for key, value in roman_numeral.items():
            while num >= value:
                roman_result += key
                num -= value
    return roman_result



print(roman_numeral_creator(test_case_one))

