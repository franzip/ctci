from lib import LinkedList


def sumDigitsWithRemainder(first, second, remainder):
    result = first + second + remainder
    hasRemainder = result >= 10
    return {
        'digit': result % 10 if hasRemainder else result,
        'remainder': result // 10 if hasRemainder else 0
    }


def sum_lists_reversed(list1: LinkedList, list2: LinkedList):
    """
    Sum the numbers represented in list1 and list2 with right to left digit order
    Returns the sum expressed as new list
    """
    ptr1, ptr2 = list1.head, list2.head
    result, remainder = [], 0

    while ptr1 or ptr2:
        sumResult = sumDigitsWithRemainder(
            (ptr1 and ptr1.data) or result[-1], (ptr2 and ptr2.data) or result[-1], remainder)
        result.append(sumResult.get('digit'))
        remainder = sumResult.get('remainder')

        if ptr1:
            ptr1 = ptr1.next
        if ptr2:
            ptr2 = ptr2.next

    remainder and result.append(remainder)

    return LinkedList(result)


def sum_list(list1: LinkedList, list2: LinkedList):
    """
    Sum the numbers represented in list1 and list2 with left to right digit order
    Returns the sum expressed as new list
    """
    ptr1, ptr2 = list1.head, list2.head
    digits, remainder = [[], []], 0
    result = []

    while ptr1 or ptr2:
        if ptr1:
            digits[0].append(ptr1.data)
            ptr1 = ptr1.next
        else:
            digits[0] = [0] + digits[0]
        if ptr2:
            digits[1].append(ptr2.data)
            ptr2 = ptr2.next
        else:
            digits[1] = [0] + digits[1]

    for i in range(len(digits[0]) - 1, -1, -1):
        sumResult = sumDigitsWithRemainder(
            digits[0][i], digits[1][i], remainder)

        result = [sumResult.get('digit')] + result
        remainder = sumResult.get('remainder')

    if remainder:
        result = [remainder] + result

    return LinkedList(result)


assert sum_lists_reversed(LinkedList(
    [8, 9, 9]), LinkedList([2])) == LinkedList([0, 0, 0, 1])
assert sum_lists_reversed(LinkedList(
    [8, 9]), LinkedList([2])) == LinkedList([0, 0, 1])
assert sum_lists_reversed(LinkedList([7, 1, 6]), LinkedList(
    [5, 9, 2])) == LinkedList([2, 1, 9])

assert sum_list(LinkedList([9, 8]), LinkedList([2])) == LinkedList([1, 0, 0])
assert sum_list(LinkedList([9, 9, 8]), LinkedList(
    [2])) == LinkedList([1, 0, 0, 0])
assert sum_list(LinkedList([6, 1, 7]), LinkedList(
    [2, 9, 5])) == LinkedList([9, 1, 2])
