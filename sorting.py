from typing import List


def bubble_sort(nums: List[int]):
    swapped = True, 0

    while swapped:
        iter, swapped = 0, False

        for index in range(len(nums) - 1 - iter):
            if nums[index + 1] < nums[index]:
                nums[index + 1], nums[index] = nums[index], nums[index + 1]
                swapped = True

            iter += 1

    return nums


def selection_sort(nums: List[int]):
    nums_len = len(nums)

    for i in range(nums_len):
        minIdx = i
        for j in range(i + 1, nums_len):
            if nums[j] < nums[minIdx]:
                minIdx = j

        nums[i], nums[minIdx] = nums[minIdx], nums[i]

    return nums


def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        curr, j = nums[i], i - 1

        while nums[j] > curr and j >= 0:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = curr

    return nums


def merge_sort(nums: List[int]):
    def merge(first_list: List[int], second_list: List[int]):
        result = []

        while len(first_list) > 0 and len(second_list) > 0:
            if first_list[0] <= second_list[0]:
                result.append(first_list[0])
                first_list = first_list[1:]
            else:
                result.append(second_list[0])
                second_list = second_list[1:]

        return result + first_list + second_list

    length = len(nums)

    if length < 2:
        return nums

    left_half = merge_sort(nums[0: length // 2])
    right_half = merge_sort(nums[length // 2:])

    return merge(left_half, right_half)


def quick_sort(nums: List[int]):
    length = len(nums)

    if length < 2:
        return nums

    pivot_idx = length // 2
    left, right = [], []

    for i in range(len(nums)):
        if i == pivot_idx:
            continue

        num = nums[i]
        if num < nums[pivot_idx]:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [nums[pivot_idx]] + quick_sort(right)


def radix_sort(nums: List[int]):
    def enqueue(nums, iter):
        result = [[] for _ in range(10)]

        for num in nums:
            bucket = (num % 10 ** iter) // (10 ** (iter - 1))
            result[bucket].append(num)

        return result

    def dequeue(buckets: List[List[int]]):
        result = []
        for bucket in buckets:
            result += bucket
        return result

    iters = len(str(max(nums)))

    def _radix_sort(nums: List[int], iter: int):
        if iter == iters:
            return nums

        return _radix_sort(dequeue(enqueue(nums, iter + 1)), iter + 1)

    return _radix_sort(nums, 0)


def heap_sort(nums: List[int]):
    size = len(nums)

    def __swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def __heapifyAt(i: int, offset):
        left_idx, right_idx = (i * 2) + 1, (i * 2) + 2
        largest_idx = i

        if left_idx < offset and nums[left_idx] > nums[largest_idx]:
            largest_idx = left_idx

        if right_idx < offset and nums[right_idx] > nums[largest_idx]:
            largest_idx = right_idx

        if largest_idx != i:
            __swap(largest_idx, i)
            __heapifyAt(largest_idx, offset)

    for i in range(size // 2 - 1, -1, -1):
        __heapifyAt(i, size)

    for i in range(size - 1, 0, -1):
        __swap(0, i)
        __heapifyAt(0, i)

    return nums


assert bubble_sort([1, 5, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert selection_sort([1, 5, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert insertion_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert quick_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert radix_sort([255, 13, 2, 5250, 120, 25, 1123]) == [
    2, 13, 25, 120, 255, 1123, 5250]
assert heap_sort([10, 20, 15, 30, 40]) == [10, 15, 20, 30, 40]
