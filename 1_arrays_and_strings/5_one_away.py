def one_away(str_a: str, str_b: str):
    """
    Checks if the two strings are one operation away.
    Possible operations: add, remove or edit a character
    """

    len_a, len_b = len(str_a), len(str_b)

    if abs(len_a - len_b) > 1:
        return False

    changed, same_length = False, len_a == len_b

    longer_str = str_a if same_length else max(str_a, str_b, key=len)
    smaller_str = str_b if same_length else min(str_b, str_b, key=len)

    for i in range(len(smaller_str)):
        j = i + 1 if not same_length and changed else i

        has_diff = smaller_str[i] != longer_str[j]

        if has_diff:
            if changed:
                return False

            changed = True

    return changed if same_length else changed or i == j


assert (one_away('pale', 'ple') == True)
assert (one_away('pales', 'pale') == True)
assert (one_away('pale', 'bale') == True)
assert (one_away('pale', 'bake') == False)
