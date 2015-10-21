
def has_palindrome_permutation(the_string):
    parity_map = {}

    for char in the_string:
        if char in parity_map:
            parity_map[char] = not parity_map[char]
        else:
            parity_map[char] = True

    odd_seen = False

    for has_odd_parity in parity_map.values():
        if has_odd_parity:
            if odd_seen:
                return False
            else:
                odd_seen = True

    return True


print(has_palindrome_permutation("livci"))
