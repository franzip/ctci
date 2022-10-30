from lib import LinkedList


def is_palindrome(list: LinkedList):
    """
    Check if list is palindrome
    """
    values, fast, slow, count = [], list.head, list.head, 0

    while fast and fast.next:
        values.append(slow.data)
        count += 1
        fast = fast.next.next
        slow = slow.next

    slow = slow.next if fast else slow

    while slow:
        if values[count - 1] != slow.data:
            return False

        count -= 1
        slow = slow.next

    return True


assert is_palindrome(LinkedList([1, 2, 3, 2, 1])) == True
assert is_palindrome(LinkedList([1, 2, 3, 4])) == False
assert is_palindrome(LinkedList([5, 6, 5])) == True
assert is_palindrome(LinkedList([1])) == True
assert is_palindrome(LinkedList([1, 2])) == False
