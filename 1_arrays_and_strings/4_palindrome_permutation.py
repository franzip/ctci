def palindrome_permutation(str: str) -> bool:
    """
    Checks if str is a permutation of a palindrome string
    """
    charMap, strLen = {}, 0

    for char in str:
        if char.isalpha():
            strLen += 1
            char_to_lower = char.lower()
            charMap[char_to_lower] = charMap.get(char_to_lower, 0) + 1

    oddFound = False

    for x in charMap.values():
        if x % 2 == 1:
            if oddFound:
                return False

            oddFound = True

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
