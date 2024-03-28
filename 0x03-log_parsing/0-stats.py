#!/usr/bin/python3
"""0-stats.py"""
import sys
from typing import Dict


def print_stats(file_size: int, status_codes: Dict[str, int]) -> None:
    """output stat"""

    print('File size:', file_size)

    for code, stat in sorted(status_codes.items(), key=lambda c: c[0]):
        print(f'{code}: {stat}')


if __name__ == '__main__':

    file_size = 0

    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    count_read = 0

    try:

        for line in sys.stdin:

            try:
                infos = line[:-1].split()

                size = int(infos[-1])
                file_size += size

                code = int(infos[-2])
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1

            except BaseException:
                pass

            count_read += 1

            if count_read % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)
