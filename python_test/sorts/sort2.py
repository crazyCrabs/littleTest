# 计数排序 适用最大值和最小值相差不大的情况
# https://blog.csdn.net/qq_44372971/article/details/107188744
def count_sort(nums: list):
    max_num = max(nums)
    bucket = [0] * (max_num + 1)
    for num in nums:
        bucket[num] += 1
    sorted_nums = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            sorted_nums.extend([i] * bucket[i])
    return sorted_nums


def count_sort1(nums: list):
    min_num, max_num = min(nums), max(nums)
    length = max_num - min_num + 1
    counts = [0] * length
    for num in nums:
        counts[num - min_num] += 1

    for i in range(1, length):
        counts[i] += counts[i - 1]

    sorted_nums = [0] * len(nums)
    for i in nums:
        sorted_nums[counts[i - min_num] - 1] = i
        counts[i - min_num] -= 1
    return sorted_nums


# 桶排序
# https://blog.csdn.net/ggdhs/article/details/90613650
def bucket_sort(nums: list, bucket_num: int = 5):
    if len(nums) <= 1:
        return nums
    min_num, max_num = min(nums), max(nums)
    bucket_size = (max_num - min_num) // bucket_num + 1
    bucket = [[] for _ in range(bucket_num)]

    for i in nums:
        bucket[(i - min_num) // bucket_size].append(i)
    # 桶内排序
    for i in range(bucket_num):
        bucket[i].sort()

    res = []
    for i in range(bucket_num):
        res.extend(bucket[i])
    return res


# 基数排序
def radix_sort(nums: list):
    n = len(str(max(nums)))
    for radix in range(n):
        buckets = [[] for _ in range(10)]
        for i in nums:
            buckets[i // (10 ** radix) % 10].append(i)
        nums = [j for i in buckets for j in i]
    return nums


if __name__ == '__main__':
    nums = [2, 15, 13, 21, 22, 18, 20, 4]
    # print(count_sort(nums.copy()))
    # print(count_sort1(nums.copy()))

    # print(bucket_sort(nums.copy(), bucket_num=8))
    print(radix_sort(nums.copy()))
