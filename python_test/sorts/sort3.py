import random


# 快速排序
# https://cloud.tencent.com/developer/article/1571782
# https://zhuanlan.zhihu.com/p/63227573
def partition(nums: list, first, last):
    mid = nums[first]
    low = first
    high = last
    while low < high:
        while low < high and nums[high] >= mid:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < mid:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid
    return low


def quick_sort(nums, first, last):
    if first >= last:
        return
    low = partition(nums, first, last)
    quick_sort(nums, first, low - 1)
    quick_sort(nums, low + 1, last)


# 随机数快速排序
def random_partition(nums: list, first, last):
    pivot = random.randint(first, last)
    nums[pivot], nums[last] = nums[last], nums[pivot]

    tmp = nums[last]
    i = first - 1
    for j in range(first, last):
        if nums[j] < tmp:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[last] = nums[last], nums[i + 1]
    return i + 1


def quick_sort_random(nums: list, left, right):
    if left < right:
        pivot = random_partition(nums, left, right)
        quick_sort_random(nums, left, pivot - 1)
        quick_sort_random(nums, pivot + 1, right)


# 三数取中法
# https://www.cnblogs.com/chengxiao/p/6262208.html
def quick_sort_median(nums):
    def partition(left, right, pivot):
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

    def get_median(left, right):
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[mid] > nums[left]:
            nums[mid], nums[left] = nums[left], nums[mid]
        return nums[left]

    def sort(left, right):
        if left >= right:
            return
        pivot = get_median(left, right)
        index = partition(left, right, pivot)
        sort(left, index - 1)
        sort(index, right)

    sort(0, len(nums) - 1)
    return nums


def partition3(nums: list, left, right):
    mid = (left + right) // 2
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    if nums[left] > nums[right]:
        nums[left], nums[right] = nums[right], nums[left]
    if nums[mid] > nums[right]:
        nums[mid], nums[right] = nums[right], nums[mid]
    nums[mid], nums[right - 1] = nums[right - 1], nums[mid]


def quick_sort3(nums: list, left, right):
    if left >= right:
        return
    partition3(nums, left, right)
    i = left + 1
    j = right - 1 - 1
    pivot = right - 1
    while True:
        while nums[i] < nums[pivot]:
            i += 1
        while nums[j] > nums[pivot]:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    if i <= right:
        nums[i], nums[right - 1] = nums[right - 1], nums[i]
    quick_sort3(nums, left, i - 1)
    quick_sort3(nums, i + 1, right)


if __name__ == '__main__':
    nums = [5, 3, 1, 9, 111, 0]

    # quick_sort(nums, 0, len(nums) - 1)
    # print(nums)

    # quick_sort_random(nums, 0, len(nums) - 1)
    # print(nums)

    print(quick_sort_median(nums))
    # quick_sort3(nums, 0, len(nums) - 1)
    # print(nums)
