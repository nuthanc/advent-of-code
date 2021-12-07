# https://adventofcode.com/2021/day/3

from os import path
THIS_DIR = path.dirname(path.realpath(__file__))
file_path = path.join(THIS_DIR, 'input.txt')
with open(file_path) as f:
    report = f.read().splitlines()

def first():
    num_len = len(report[0])
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(num_len):
        num_zeroes = 0
        for j in range(len(report)):
            if report[j][i] == '0':
                num_zeroes += 1
        if num_zeroes > (len(report) - num_zeroes):
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
            
    gamma_rate = (int(gamma_rate, 2))
    epsilon_rate = (int(epsilon_rate, 2))
    print(gamma_rate * epsilon_rate)

# first()

def generate_rating(report_copy, comparator):
    num_len = len(report_copy[0])

    for i in range(num_len):
        if len(report_copy) > 1:
            zero_prefix = []
            one_prefix = []
            for j in range(len(report_copy)):
                if report_copy[j][i] == '0':
                    zero_prefix.append(report_copy[j])
                else:
                    one_prefix.append(report_copy[j])
            if comparator(zero_prefix, one_prefix):
                report_copy = zero_prefix
            else:
                report_copy = one_prefix
        else:
            break
    return report_copy[0]

def second(report):
    oxygen_generator = generate_rating(
        report.copy(), lambda a, b: len(a) > len(b))
    co2_scrubber = generate_rating(
        report.copy(), lambda a, b: len(a) <= len(b))
    
    oxygen_generator_rating = int(oxygen_generator,2)
    co2_scrubber_rating = int(co2_scrubber, 2)
    print(oxygen_generator_rating * co2_scrubber_rating)

second(report)
