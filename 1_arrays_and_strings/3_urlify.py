def urlify(str: str) -> str:
    """
    Replaces spaces with %20
    """
    token, result = '', []

    for i in range(len(str)):
        if str[i] == ' ' and str[i - 1] != ' ':
            result.append(token)
            token = ''
        else:
            token += str[i]

    return "%20".join(result)


assert urlify("Mr John Smith      ") == "Mr%20John%20Smith"
