def part_one():
    with open('input.txt') as f:
        lines = f.readlines()

    start = {}
    for line in lines:
        number = ''.join(x for x in line if x.isdigit())
        for x in range(len(number)):
            start[x] = start.get(x, 0) + int(number[x])

    g = [(1 if v > (len(lines) / 2) else 0) for k, v in start.items()]
    e = [(1 if v < (len(lines) / 2) else 0) for k, v in start.items()]
    gamma = 0
    for bit in g:
        gamma = (gamma << 1) | bit

    epsilon = 0
    for bit in e:
        epsilon = (epsilon << 1) | bit

    return epsilon * gamma

def part_two():
    with open('input.txt') as f:
        lines = f.readlines()


if __name__ == '__main__':
    print(part_one())
    print(part_two())
