def is_unique(str: str) -> bool:
    """
    Checks whether str contains all unique characters
    """
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True


assert is_unique('abc') == True
assert is_unique('abcda') == False
