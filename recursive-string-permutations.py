def get_permutations(string):
    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    possible_positions_to_put_last_char = range(len(all_chars_except_last)+1)
    permutations = []
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in possible_positions_to_put_last_char:
            # permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            # permutation = last_char + permutation_of_all_chars_except_last[:position] + permutation_of_all_chars_except_last[position:]
            permutation = permutation_of_all_chars_except_last[position:] + last_char + permutation_of_all_chars_except_last[:position]
            # p1 = permutation_of_all_chars_except_last[:position]
            # print("p1 " + p1)
            # p2 = last_char
            # print("p2 " + p2)
            # p3 = permutation_of_all_chars_except_last[position:]
            # print("p3 " + p3)
            # permutation = p1 + p2 + p3
            # print(permutation)
            permutations.append(permutation)
    return permutations

print(get_permutations("cats"))
