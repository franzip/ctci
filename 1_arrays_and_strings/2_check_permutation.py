def check_permutation(str1: str, str2: str) -> bool:
    """
    Checks if a is a permutation of b
    """
    if len(str1) != len(str2):
        return False

    char_count1, char_count2 = {}, {}

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    return char_count1 == char_count2


assert check_permutation("abc", "bca") == True
assert check_permutation("zqw", "wqa") == False
