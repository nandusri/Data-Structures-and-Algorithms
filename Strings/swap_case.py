"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
Pythonist → pYTHONIST
"""


def swap_case(s):
    converted_string = ""
    for char in s:
        if char.isupper():
            converted_string += char.lower()
        elif char.islower():
            converted_string += char.upper()
        else:
            converted_string += char
    return converted_string


s = input()
result = swap_case(s)
print(result)
