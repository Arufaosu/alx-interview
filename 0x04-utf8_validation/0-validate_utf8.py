#!/usr/bin/python3
"""0-validate_utf8.py"""
from typing import List

def validUTF8(data: List[int]) -> bool:
    """checks if int is valid or not"""

    def single_UTF8_byte(byte: int) -> bool:
        return True if byte >> 7 & 1 == 0 else False

    def continuation_UTF8_byte(byte: int) -> bool:
        """checks if byte represents a continuation UTF-8 byte"""
        if byte >> 7 & 1 == 1 and byte >> 6 & 1 == 0:
            return True
        else:
            return False

    def two_UTF8_byte(byte: int) -> bool:
        """checks if the byte starts a 2-byte UTF-8 grapheme"""
        if byte >> 7 & 1 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 0:
            return True
        else:
            return False

    def three_UTF8_byte(byte: int) -> bool:
        """checks if the byte starts a 3-byte UTF-8 grapheme"""
        if byte >> 7 & 1 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 1\
                and byte >> 4 & 1 == 0:
            return True
        else:
            return False

    def four_UTF8_byte(byte: int) -> bool:
        """checks if the byte starts a 4-byte UTF-8 grapheme"""
        if byte >> 7 & 1 == 1 and byte >> 6 & 1 == 1 and byte >> 5 & 1 == 1\
                and byte >> 4 & 1 == 1 and byte >> 3 & 1 == 0:
            return True
        else:
            return False

    total_bytes = len(data)
    idx = 0

    while idx < total_bytes:
        byte = data[idx]

        if single_UTF8_byte(byte):
            idx += 1
            continue

        elif two_UTF8_byte(byte):
            if idx > total_bytes - 2 or\
                    not continuation_UTF8_byte(data[idx + 1]):
                return False

            idx += 2
            continue

        elif three_UTF8_byte(byte):
            if idx > total_bytes - 3 or\
                    not continuation_UTF8_byte(data[idx + 1]) or\
                    not continuation_UTF8_byte(data[idx + 2]):
                return False

            idx += 3
            continue

        elif four_UTF8_byte(byte):
            if idx > total_bytes - 4 or\
                    not continuation_UTF8_byte(data[idx + 1]) or\
                    not continuation_UTF8_byte(data[idx + 2]) or\
                    not continuation_UTF8_byte(data[idx + 3]):
                return False

            idx += 4
            continue
        else:
            return False

    return True
