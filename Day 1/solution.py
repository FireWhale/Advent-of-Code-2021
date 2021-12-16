def solve():
    with open('input.txt') as f:
        lines = f.readlines()

    prev_value = int(lines[0]) + 1
    counter = 0
    for line in lines:
        if int(line) > prev_value:
            counter += 1
        prev_value = int(line)

    return counter


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [int(l) for l in lines]

    counter = 0
    for i in range(len(lines) - 3):
        # string = f"{lines[i]}, {lines[i+1]}, {lines[i+2]}, {lines[i+3]} | {sum(lines[i:i+3])} < {sum(lines[i+1:i+4])}"
        if lines[i] < lines[i + 3]:
            # print(f"Increased: {string} ")
            counter += 1
        else:
            pass
            # print(f"Decreased: {string}")

    return counter


if __name__ == '__main__':
    print(solve())
    print(part_two())
