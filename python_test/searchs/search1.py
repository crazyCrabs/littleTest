# 二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def recurse_binary_search(nums: list, left: int, right: int, value: int):
    if left > right:
        return
    mid = left + ((right - left) >> 1)
    if nums[mid] == value:
        return mid
    elif nums[mid] > value:
        return recurse_binary_search(nums, left, mid - 1, value)
    elif nums[mid] < value:
        return recurse_binary_search(nums, mid + 1, right, value)


# 二分查找变形
# 1.查找第一个值等于给定值的元素
def binary_search_1(nums: list, value: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > value:
            high = mid - 1
        elif nums[mid] < value:
            low = mid + 1
        elif mid == 0 or nums[mid - 1] != value:
            return mid
        else:
            high = mid - 1


def binary_search_1_0(nums: list, value: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(nums) and nums[low] == value:
        return low


# 2.查找最后一个值等于给定值的元素
def binary_search_2(nums: list, value: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > value:
            high = mid - 1
        elif nums[mid] < value:
            low = mid + 1
        elif mid == len(nums) - 1 or nums[mid + 1] != value:
            return mid
        else:
            low = mid + 1


def binary_search_2_0(nums: list, value: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] <= value:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] == value:
        return high


if __name__ == '__main__':
    my_list = [1, 3, 5, 5, 5, 7, 9]
    # print(binary_search(my_list, 3))
    # print(recurse_binary_search(my_list, 0, len(my_list) - 1, 3))

    print(binary_search_1(my_list, 5))
    print(binary_search_2_0(my_list, 5))
