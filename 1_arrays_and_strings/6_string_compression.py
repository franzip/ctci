def string_compression(str: str):
    """
    Compress basic string compression
    """
    strLen, result = len(str), ""
    count, i = 0, 0

    while i < strLen - 1:
        if i != strLen - 1 and str[i + 1] != str[i]:
            result = f"{result}{str[i]}{count+1}"
            count = 0
        else:
            count += 1

        i += 1

    result = f"{result}{str[i]}{count + 1}"

    return str if strLen <= len(result) else result


assert string_compression("aabcccccaaa") == "a2b1c5a3"
assert string_compression("abcdefg") == "abcdefg"
assert string_compression("a") == "a"
