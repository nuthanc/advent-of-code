'''
1. Verify the Constraints
    * Alphabets only from a through g(Lowercase)
    * Signal Patterns in any Order(10 separated by Space)
    * No Repeats
    * Determine how many times do digits 1,4,7 or 8 appear
2. Write down some Test Cases
3. Solution without code
    * For First Solution
        * In the four_digit part, sum occurences of 2,3,4,7 characters
    * For Second Solution
        * Important parameters: 
            * Length to Digit mapping- 2:(1), 3:(7), 4:(4), 5:(2,3,5), 6:(0,6,9), 7:(8)
            * Map each of the seven digit display with numbers 1 to 7, starting from top and moving left to right
                        1
                    2       3
                        4
                    5       6
                        7
            * Now, map these to numbers 0 to 9
            * {
                0: (1,2,3,5,6,7),
                1: (3,6),
                2: (1,3,4,5,7),
                3: (1,3,4,6,7),
                4: (2,3,4,6),
                5: (1,2,4,6,7),
                6: (1,2,4,5,6,7),
                7: (1,3,6),
                8: (1,2,3,4,5,6,7),
                9: (1,2,3,4,6,7)
            }
        * Comparing each unique patterns to determine the correct segment
            * Len 2 and 3
            * Len 3 and 4
            * Len 4 and 7
            * Len 4 and 5(find pattern of Len 5 with only 2 matches with 4 cause that would be 2. 3 and 5 will have 3 matches)
            * Len 4 and 6(find pattern of Len 6 with only 4 matches cause that would be 9. 0 and 6 will have 3 matches)
            
4. Solution with code
5. Double Check for Errors
6. Walk through the Test Case
7. Time & Space Complexity
8. Optimize the Solution
'''
from os import path


def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        entries = f.read().splitlines()
    return entries


def first(entries):
    times = 0
    for entry in entries:
        patterns, four_digit_chars = entry.split(' | ')
        for digit_chars in four_digit_chars.split():
            length = len(digit_chars)
            if length == 2 or length == 3 or length == 4 or length == 7:
                times += 1
    print(times)


def match_with_len_4_and_extract_chars(first_pattern, second_patterns, first_pattern_digits, num_of_matches, digit, digit_mappings, char_digit_mappings, num_set):
    for second_pattern in second_patterns:
        if len(second_pattern.intersection(first_pattern)) == num_of_matches:
            unique_chars = second_pattern.symmetric_difference(first_pattern)
            second_pattern_digits = digit_mappings.get(digit)
            unique_digits = first_pattern_digits.symmetric_difference(
                second_pattern_digits)

            for char, digit_set in char_digit_mappings.items():
                if len(digit_set) == 1 and next(iter(digit_set)) not in num_set:
                    num_set.add(next(iter(digit_set)))
                if char in unique_chars:
                    if len(digit_set - unique_digits) == 1:
                        common_digit_set = digit_set.intersection(
                            unique_digits)
                        char_digit_mappings[char] = common_digit_set
                        num = next(iter(common_digit_set))
                        if num not in num_set:
                            num_set.add(num)
                        for nested_char, nested_digit_set in char_digit_mappings.items():
                            if nested_char != char:
                                common_in_nested = common_digit_set.intersection(
                                    nested_digit_set)
                                if len(common_in_nested) == 1:
                                    unique_in_nested = nested_digit_set - common_digit_set
                                    char_digit_mappings[nested_char] = unique_in_nested
                                    num = next(iter(unique_in_nested))
                                    if num not in num_set:
                                        num_set.add(num)
                                    break
                    unique_chars.remove(char)
                    # Can also use unique_digits.difference(digit_set)
                    unique_digits = unique_digits - digit_set
            for char in unique_chars:
                char_digit_mappings[char] = unique_digits
            break


def get_digit_mappings():
    return {
        0: set((1, 2, 3, 5, 6, 7)),
        1: set((3, 6)),
        2: set((1, 3, 4, 5, 7)),
        3: set((1, 3, 4, 6, 7)),
        4: set((2, 3, 4, 6)),
        5: set((1, 2, 4, 6, 7)),
        6: set((1, 2, 4, 5, 6, 7)),
        7: set((1, 3, 6)),
        8: set((1, 2, 3, 4, 5, 6, 7)),
        9: set((1, 2, 3, 4, 6, 7))
    }


def get_char_to_digit_mappings(patterns, digit_mappings, num_length_mappings):
    pattern_len_mappings = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    char_digit_mappings = {}
    for pattern in patterns.split():
        pattern_length = len(pattern)
        pattern_len_mappings[pattern_length].append(set(pattern))

    unique_lengths = (2, 3, 4, 7)
    for i in range(len(unique_lengths)-1):
        first_patter_len = unique_lengths[i]
        second_pattern_len = unique_lengths[i+1]
        first_pattern = pattern_len_mappings[first_patter_len][0]
        second_pattern = pattern_len_mappings[second_pattern_len][0]
        first_pattern_digits = digit_mappings[num_length_mappings[first_patter_len][0]]
        second_pattern_digits = digit_mappings[num_length_mappings[second_pattern_len][0]]
        unique_chars = second_pattern.symmetric_difference(
            first_pattern)  # Can also use second_pattern ^ first_pattern
        unique_digits = first_pattern_digits.symmetric_difference(
            second_pattern_digits)
        for char, digit_set in char_digit_mappings.items():
            if char in unique_chars:
                unique_chars.remove(char)
                # Can also use unique_digits.difference(digit_set)
                unique_digits = unique_digits - digit_set
        for char in unique_chars:
            char_digit_mappings[char] = unique_digits

    # Match with len 4 and (5,6) to get remaining character mappings
    lengths = (5, 6)
    first_pattern_len = 4
    first_pattern = pattern_len_mappings[first_patter_len][0]
    first_pattern_digits = digit_mappings.get(4)
    num_set = set()
    for second_pattern_len in lengths:
        second_patterns = pattern_len_mappings[second_pattern_len]
        if second_pattern_len == 5:
            match_with_len_4_and_extract_chars(first_pattern, second_patterns, first_pattern_digits, num_of_matches=2,
                                               digit=2, digit_mappings=digit_mappings, char_digit_mappings=char_digit_mappings, num_set=num_set)
        else:
            match_with_len_4_and_extract_chars(first_pattern, second_patterns, first_pattern_digits, num_of_matches=4,
                                               digit=9, digit_mappings=digit_mappings, char_digit_mappings=char_digit_mappings, num_set=num_set)

    all_char_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    missing_char = next(iter(all_char_set - char_digit_mappings.keys()))
    all_num_set = {1, 2, 3, 4, 5, 6, 7}
    missing_num = all_num_set - num_set
    char_digit_mappings[missing_char] = missing_num

    return char_digit_mappings


def second(entries):
    total_output = 0
    digit_mappings = get_digit_mappings()
    num_length_mappings = {2: (1,), 3: (7,), 4: (
        4,), 5: (2, 3, 5), 6: (0, 6, 9), 7: (8,)}

    for entry in entries:
        patterns, four_digit_chars = entry.split(' | ')
        num_string = ''
        four_digit_chars = four_digit_chars.split()
        for digit_chars in four_digit_chars:
            digit_chars_length = len(digit_chars)
            number_tuples = num_length_mappings.get(digit_chars_length)
            if len(number_tuples) == 1:
                num_string += str(number_tuples[0])
        if len(num_string) == 4:
            total_output += int(num_string)
        else:
            char_digit_mappings = get_char_to_digit_mappings(
                patterns, digit_mappings, num_length_mappings)
            # print(char_digit_mappings)
            num_string = ''
            for digit_chars in four_digit_chars:
                digit_chars_length = len(digit_chars)
                number_tuples = num_length_mappings.get(digit_chars_length)

                if len(number_tuples) == 1:
                    num_string += str(number_tuples[0])

                else:
                    digit_set = set()
                    for char in digit_chars:
                        digit = next(iter(char_digit_mappings[char]))
                        digit_set.add(digit)

                    for digit, mappings_set in digit_mappings.items():
                        if len(mappings_set.symmetric_difference(digit_set)) == 0:
                            num_string += str(digit)
                            break
            total_output += int(num_string)
    print(total_output)


def solution():
    entries = read_file()
    # first(entries.copy())
    second(entries)


solution()
