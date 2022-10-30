def div(a: int, b: int):
    def recursive_div(a: int, b: int, c: int):
        if a < b:
            return c
        return recursive_div(a - b, b, c + 1)
    return recursive_div(a, b, 0)


def distinct_int(arr, diff):
    pairs = []
    cache = {}

    for element in arr:
        cache[element] = element
        sumMatch = cache.get(element + diff)
        diffMatch = cache.get(element - diff)

        if sumMatch:
            pairs.append((sumMatch, element))
        if diffMatch:
            pairs.append((diffMatch, element))

    return pairs


def find_substring_permutations(longer, shorter):
    char_map = {char: shorter.count(char) for char in shorter}
    shorter_len, idx = len(shorter), 0
    results = []

    while idx < len(longer) - shorter_len + 1:
        substring = longer[idx: idx + shorter_len]
        substring_map = dict(char_map)

        for substr_idx in range(shorter_len):
            substr_char = substring[substr_idx]
            substring_map_char = char_map.get(substr_char)
            if not substring_map_char:
                idx += substr_idx
                break

            substring_map[substr_char] = substring_map.get(substr_char, 0) - 1

        if all(x == 0 for x in substring_map.values()):
            results.append(substring)

        idx += 1

    return results


def find_all_permutations(str):
    result = []

    def find_all(str, prefix):
        if len(str) == 0:
            result.append(prefix)
        for i in range(len(str)):
            rem = str[0:i] + str[i+1:]
            find_all(rem, prefix + str[i])

    find_all(str, '')
    return result


print(find_all_permutations('abcd'))
