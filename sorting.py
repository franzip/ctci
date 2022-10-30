def bubble_sort(nums):
    swapped = True, 0

    while swapped:
        iter, swapped = 0, False

        for index in range(len(nums) - 1 - iter):
            if nums[index + 1] < nums[index]:
                nums[index + 1], nums[index] = nums[index], nums[index + 1]
                swapped = True

            iter += 1

    return nums


def selection_sort(nums):
    numsLen = len(nums)

    for i in range(numsLen):
        minIdx = i
        for j in range(i + 1, numsLen):
            if nums[j] < nums[minIdx]:
                minIdx = j

        nums[i], nums[minIdx] = nums[minIdx], nums[i]

    return nums


def insertion_sort(nums):
    numsLen = len(nums)

    for i in range(1, numsLen):
        curr, j = nums[i], i - 1

        while nums[j] > curr and j >= 0:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = curr

    return nums


def merge(sNums1, sNums2):
    result = []

    while len(sNums1) > 0 and len(sNums2) > 0:
        if sNums1[0] <= sNums2[0]:
            result.append(sNums1[0])
            sNums1 = sNums1[1:]
        else:
            result.append(sNums2[0])
            sNums2 = sNums2[1:]

    return result + sNums1 + sNums2


def merge_sort(nums):
    length = len(nums)

    if length < 2:
        return nums

    sNums1 = merge_sort(nums[0: length // 2])
    sNums2 = merge_sort(nums[length // 2:])

    return merge(sNums1, sNums2)


def quick_sort(nums):
    length = len(nums)

    if length < 2:
        return nums

    pivotIdx = length // 2
    left, right = [], []

    for i in range(len(nums)):
        if i == pivotIdx:
            continue

        num = nums[i]
        if num < nums[pivotIdx]:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [nums[pivotIdx]] + quick_sort(right)


def radix_sort(nums):
    def enqueue(nums, iter):
        result = [[] for _ in range(10)]

        for num in nums:
            bucket = (num % 10 ** iter) // (10 ** (iter - 1))
            result[bucket].append(num)

        return result

    def dequeue(buckets):
        result = []
        for bucket in buckets:
            result += bucket
        return result

    iters = len(str(max(nums)))

    def _radix_sort(nums, iter):
        if iter == iters:
            return nums

        return _radix_sort(dequeue(enqueue(nums, iter + 1)), iter + 1)

    return _radix_sort(nums, 0)


assert bubble_sort([1, 5, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert selection_sort([1, 5, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert insertion_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert quick_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
assert radix_sort([255, 13, 2, 5250, 120, 25, 1123]) == [
    2, 13, 25, 120, 255, 1123, 5250]
