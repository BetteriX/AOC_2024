#!/usr/bin/env python3


def main():
    f = open("input", "r")

    lines = f.read().splitlines()

    left = []
    right = {}
    for line in lines:
        parts = line.split()

        left.append(parts[0])

        if right.get(parts[1]):
            right[parts[1]] += 1
        else:
            right[parts[1]] = 1

    total = 0

    for num in left:
        if right.get(num):
            total += int(num) * right.get(num)

    print("Total Distance:", str(total))


if __name__ == "__main__":
    main()
