def read_data():
    data = []
    with open('1/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            val = line.strip()
            data.append(int(val))
    return data

def count_increases(data, window = 3):
    total = 0

    for i in range(len(data) - (window - 1)):
        first_sum = sum(data[i:(i+window)])
        second_sum = sum(data[(i+1):(i+window+1)])
        if i == 0:
        if second_sum > first_sum:
            total += 1
    return total


def main():
    data = read_data()
    increases = count_increases(data)
    print(f'total increases is {increases}')


if __name__ == '__main__':
    main()

