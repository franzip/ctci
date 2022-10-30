def one_away(strA: str, strB: str):
    """
    Checks if the two strings are one operation away.
    Possible operations: add, remove or edit a character
    """

    lenA, lenB = len(strA), len(strB)

    if abs(lenA - lenB) > 1:
        return False

    changed, sameLength = False, lenA == lenB

    maxStr = strA if sameLength else max(strA, strB, key=len)
    minStr = strB if sameLength else min(strB, strB, key=len)

    for i in range(len(minStr)):
        j = i + 1 if not sameLength and changed else i

        hasDiff = minStr[i] != maxStr[j]

        if hasDiff:
            if changed:
                return False

            changed = True

    return changed if sameLength else changed or i == j


assert (one_away('pale', 'ple') == True)
assert (one_away('pales', 'pale') == True)
assert (one_away('pale', 'bale') == True)
assert (one_away('pale', 'bake') == False)
