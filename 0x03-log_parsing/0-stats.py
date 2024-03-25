#!/usr/bin/python3
"""script that reads stdin line by line"""
import sys
import re

def print_statistics(total_file_size, status_counts):
    """print stats"""
    print("File size:", total_file_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def parse_line(line):
    """define a regex pattern to extract relevant information from the log line"""
    pattern = r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

    match = re.match(pattern, line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        return status_code, file_size
    else:
        return None, None

def main():
    total_file_size = 0
    status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    lines_processed = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
                lines_processed += 1

            if lines_processed == 10:
                print_statistics(total_file_size, status_counts)
                lines_processed = 0

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
