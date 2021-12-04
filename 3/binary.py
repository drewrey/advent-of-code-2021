def read_data():
    data = []
    with open('3/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            number = line.strip()
            data.append(number)
    return data

def find_gamma_rate(numbers):
    num_digits = len(numbers[0])
    total_numbers = len(numbers)
    counts_of_ones = {}
    for i in range(num_digits):
        counts_of_ones[i] = 0
    for num in numbers:
        for i in range(num_digits):
            if num[i] == '1':
                counts_of_ones[i] += 1
    output = ''
    for i in range(num_digits):
        if counts_of_ones[i] > (total_numbers / 2):
            output += '1'
        else:
            output += '0'

    return output

def find_epsilon_rate(gamma_rate):
    num_digits = len(gamma_rate)
    epsilon_rate = ''
    for _, val in enumerate(gamma_rate):
        if val == '0':
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'
    return epsilon_rate

def main():
    numbers = read_data()
    gamma_rate = find_gamma_rate(numbers)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    print(f'gamma_rate is {gamma_rate}')
    print(f'epsilon_rate is {epsilon_rate}')
    print(f'multiplication is {int(gamma_rate, 2) * int(epsilon_rate, 2)}')


if __name__ == '__main__':
    main()
