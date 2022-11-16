def palindrome_permutation(str: str) -> bool:
    """
    Checks if str is a permutation of a palindrome string
    """
    char_map, str_len = {}, 0

    for char in str:
        if char.isalpha():
            str_len += 1
            char_to_lower = char.lower()
            char_map[char_to_lower] = char_map.get(char_to_lower, 0) + 1

    odd_found = False

    for x in char_map.values():
        if x % 2 == 1:
            if odd_found:
                return False

            odd_found = True

    return True


assert (palindrome_permutation("a") == True)
assert (palindrome_permutation("aa b") == True)
assert (palindrome_permutation("ra ar") == True)
assert (palindrome_permutation("ba aa ab") == True)
assert (palindrome_permutation("b a a caac") == True)
assert (palindrome_permutation("abc") == False)
assert (palindrome_permutation("abad") == False)
assert (palindrome_permutation("baaacb") == False)
assert (palindrome_permutation("Tact Coa") == True)
assert (palindrome_permutation("Tact Cob") == False)
assert (palindrome_permutation("oTact Ca") == True)
assert (palindrome_permutation("obbbo") == True)
assert (palindrome_permutation("baaacbc") == True)
assert (palindrome_permutation("tact coao") == True)
assert (palindrome_permutation("fo oofff") == True)
assert (palindrome_permutation("abc ab") == True)
assert (palindrome_permutation("abab") == True)
assert (palindrome_permutation("bbcccdddd") == True)
