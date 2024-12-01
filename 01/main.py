#!/usr/bin/env python3


def main():
    f = open("input", "r")

    lines = f.read().splitlines()

    right = []
    left = []
    for line in lines:
        parts = line.split()

        right.append(parts[0])
        left.append(parts[1])

    right.sort()
    left.sort()

    total_distance = 0
    for i in range(0, len(right)):
        total_distance += abs(int(right[0]) - int(left[0]))

        right.pop(0)
        left.pop(0)

    print("Total Distance:", str(total_distance))


if __name__ == "__main__":
    main()
