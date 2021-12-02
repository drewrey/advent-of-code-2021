def read_data():
    data = []
    with open('1/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            val = line.strip()
            data.append(int(val))
    return data

def count_increases(data):
    total = 0
    for i, val in enumerate(data):
        if i == 0:
            continue
        if val > data[i-1]:
            total += 1
    return total


def main():
    data = read_data()
    increases = count_increases(data)
    print(f'total increases is {increases}')


if __name__ == '__main__':
    main()

