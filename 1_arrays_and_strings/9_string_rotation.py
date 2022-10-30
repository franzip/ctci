def is_substring(str1: str, str2: str) -> bool:
    return str2 in str1


def string_rotation(str1: str, str2: str) -> bool:
    """
    Check if a str2 is a rotation of str1
    """
    if len(str1) != len(str2):
        return False

    found, start_substr, rotation_idx = False, 0, 0

    for idx in range(len(str1)):
        if str1[start_substr] == str2[idx]:
            rotation_idx = idx if not found else rotation_idx
            found = True
            start_substr += 1
        else:
            start_substr, found = 0, False

    return found and is_substring(str1, str2[0:rotation_idx])


assert string_rotation('ewaterbottl', 'waterbottle') == True
assert string_rotation('erbottlewat', 'waterbottle') == True
assert string_rotation('bottlewater', 'waterbottle') == True
assert string_rotation('bottlewater', 'waterbottle') == True
assert string_rotation('aabbccdd', 'bccddaab') == True
assert string_rotation('bottlewater', 'wtaerbottle') == False
assert string_rotation('abc', 'acb') == False
