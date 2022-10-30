def check_permutation(str1: str, str2: str) -> bool:
    """
    Checks if a is a permutation of b
    """
    if len(str1) != len(str2):
        return False

    charCount1, charCount2 = {}, {}

    for char in str1:
        charCount1[char] = charCount1.get(char, 0) + 1
    for char in str2:
        charCount2[char] = charCount2.get(char, 0) + 1

    return charCount1 == charCount2


assert check_permutation("abc", "bca") == True
assert check_permutation("zqw", "wqa") == False
