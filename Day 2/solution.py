def part_one():
    with open('input.txt') as f:
        lines = f.readlines()

    horizontal = 0
    vert = 0
    for line in lines:
        number = int(''.join(x for x in line if x.isdigit()))

        # Can a sub go negative, do I have to think about that
        if 'forward' in line:
            horizontal += number
        else:
            vert += number if 'down' in line else -1 * number

    return horizontal * vert


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()

    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        number = int(''.join(x for x in line if x.isdigit()))

        # Can a sub go negative, do I have to think about that
        if 'forward' in line:
            horizontal += number
            depth += aim * number
        else:
            aim += number if 'down' in line else -1 * number
    print(horizontal, depth, aim)

    return horizontal * depth

if __name__ == '__main__':
    print(part_one())
    print(part_two())
