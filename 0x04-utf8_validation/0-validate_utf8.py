#!/usr/bin/python3
"""0-validate_utf8.py"""

def validUTF8(data):
    def checkLeadingOnes(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        leading_ones = 0
        byte = data[i]

        if byte & 0b10000000 == 0:
            leading_ones = 0
        elif byte & 0b11100000 == 0b11000000:
            leading_ones = 1
        elif byte & 0b11110000 == 0b11100000:
            leading_ones = 2
        elif byte & 0b11111000 == 0b11110000:
            leading_ones = 3
        else:
            return False

        for j in range(1, leading_ones + 1):
            if i + j >= len(data) or not checkLeadingOnes(data[i + j]):
                return False

        i += leading_ones + 1

    return True

data1 = [65]
print(validUTF8(data1))

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))

data3 = [229, 65, 127, 256]
print(validUTF8(data3))
