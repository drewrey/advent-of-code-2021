def read_data():
    data = []
    with open('2/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            command = line.strip()
            data.append(command)
    return data

def parse_instructions(instructions):
    horizontal, depth, aim = (0, 0, 0)
    for instruction in instructions:
        command, distance = instruction.split(' ')
        distance = int(distance)
        if command == 'forward':
            horizontal += distance
            depth += aim * distance
        if command == 'down':
            aim += distance
        if command == 'up':
            aim -= distance
    return (horizontal, depth)

def main():
    commands = read_data()
    horizontal, depth = parse_instructions(commands)
    print(f'total horizontal is {horizontal}')
    print(f'total depth is {depth}')
    print(f'multiplication is {horizontal * depth}')


if __name__ == '__main__':
    main()
