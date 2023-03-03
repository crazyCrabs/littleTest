# 线性排序
import time
import sys
sys.setrecursionlimit(1000000)


# 冒泡排序
def bubble_sort(nums: list):
    a = time.time()
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print("冒泡：", time.time() - a)


# 插入排序
def insert_sort(nums: list):
    a = time.time()
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = tmp
    print("插入：", time.time() - a)


# 希尔排序 是插入排序的改进版 封神
def shell_sort(arr: list):
    a = time.time()
    length = len(arr)
    dist = length // 2

    while dist > 0:
        for i in range(dist, length):
            temp = arr[i]
            j = i
            while j >= dist and temp < arr[j-dist]:
                arr[j] = arr[j-dist]
                j -= dist
            arr[j] = temp
        dist //= 2
    print("希尔1：", time.time() - a)


# 选择排序
def select_sort(nums: list):
    a = time.time()
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print("选择：", time.time() - a)


# 归并排序 https://www.cnblogs.com/pythonbao/p/10800699.html
def merge_sort(nums: list):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return _sort(merge_sort(left), merge_sort(right))


def _sort(left: list, right: list):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


# 快速排序
def quick_sort(nums: list):
    if len(nums) <= 1:
        return nums
    mid = nums[len(nums) // 2]
    left = [i for i in nums if i < mid]
    _mid = [i for i in nums if i == mid]
    right = [i for i in nums if i > mid]
    return quick_sort(left) + _mid + quick_sort(right)


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3] * 10000
    # bubble_sort(nums.copy())
    # insert_sort(nums.copy())
    # shell_sort(nums.copy())
    # select_sort(nums.copy())

    # 分治
    a = time.time()
    print(merge_sort(nums.copy()), time.time() - a)
    # a = time.time()
    # print(quick_sort(nums.copy()), time.time() - a)
