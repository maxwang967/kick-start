# 题目：不修改数组找出重复的数字
# 在一个长度为n+1的数组里的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。
# 请找出数组中任意一个重复的数字，但不能修改输入的数组。例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，
# 那么对应的输出是重复的数字2或者3。

nums = [2,3,5,4,3,2,6,7]

def count_range(nums, start, end):
    print(f"start2={start}, end2={end}")
    if nums is None:
        return 0
    length = len(nums)
    count = 0
    for i in range(length):
        if nums[i] >= start and nums[i] <= end:
            count += 1
    return count

def get_duplication(nums):
    if nums is None:
        return 0
    length = len(nums)
    start = 1
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        count = count_range(nums, start, middle)
        if start == end:
            print(f"count={count}")
            print(f"start={start}, end={end}")
            if count > 1:
                return start
            else:
                break
        print(f"middle2={middle}")
        print(f"count2={count}")
        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return -1

print(get_duplication(nums))
