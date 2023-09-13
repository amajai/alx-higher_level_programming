#!/usr/bin/python3
"""
This script that reads stdin line by line and computes metrics

"""
import sys


sum = 0
count = 0
codes = {}

if __name__ == "__main__":
    while True:
        try:
            for line in sys.stdin:
                status_code, file_size = line.split('"')[-1].strip().split(" ")

                sum += int(file_size)
                if codes.get(status_code):
                    codes[status_code] += 1
                else:
                    codes[status_code] = 1

                count += 1
                if count == 10:
                    print("File size: {:d}".format(sum))
                    for code, size in sorted(codes.items()):
                        print("{}: {:d}".format(code, size))
                    count = 0
        except KeyboardInterrupt:
            print("File size: {:d}".format(sum))
            for code, size in sorted(codes.items()):
                print("{}: {:d}".format(code, size))
            break
