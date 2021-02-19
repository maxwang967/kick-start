class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1 selection sort (TOL)
        # l = len(nums)
        # for i in range(l - 1):
        #     min = i
        #     for j in range(i + 1, l):
        #         if nums[j] < nums[min]:
        #             min = j
        #     nums[i], nums[min] = nums[min], nums[i]
        # return nums
        # 2 bubble sort (TOL)
        # l = len(nums)
        # for j in range(l - 1, 0, -1):
        #     for i in range(0, j):
        #         if nums[i] > nums[i + 1]:
        #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # return nums
        # 3 insertion sort
        # n = len(nums)
        # for i in range(1, n):
        #     cur = i
        #     while cur > 0 and nums[cur] < nums[cur - 1]:
        #         nums[cur], nums[cur - 1] = nums[cur - 1], nums[cur]
        #         cur -= 1
        # return nums
        # 4 merge sort
        # def merge_sort(nums, left, right):
        #     # divide into sub-arrays
        #     if left >= right: return
        #     mid = (left + right) // 2
        #     merge_sort(left, mid)
        #     merge_sort(mid + 1, right)

        #     # merge
        #     temp = [0 for _ in range(right - left + 1)]
        #     i = left
        #     j = mid + 1
        #     cur = 0
        #     while i <= mid and j <= right:
        #         if nums[i] <= nums[j]:
        #             temp[cur] = nums[i]
        #             i += 1
        #             cur += 1
        #         else:
        #             temp[cur] = nums[j]
        #             j += 1
        #             cur += 1
        #     while i <= mid:
        #         temp[cur] = nums[i]
        #         cur += 1
        #         i += 1
        #     while j <= right:
        #         temp[cur] = nums[j]
        #         cur += 1
        #         j += 1
            
        #     # replace into original nums
        #     for k in range(len(temp)):
        #         nums[left + k] = temp[k]
        # n = len(nums)
        # merge_sort(nums, 0, n - 1)
        # return nums
        # 5 quick sort
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(lo, hi):
            # 取左侧第一个数字作为分界点
            pivot = nums[lo]
            i = lo + 1
            j = hi
            while True:
                while nums[i] < pivot:
                    if i == hi:
                        break
                    i += 1
                while nums[j] > pivot:
                    if j == lo:
                        break
                    j -= 1
                if i >= j:
                    break
                # print(nums)
                swap(i, j)
                # print(nums)
            swap(lo, j)
            return j


        def quick_sort(lo, hi):
            if lo >= hi:
                return
            p = partition(lo, hi)
            quick_sort(lo, p - 1)
            quick_sort(p + 1, hi)

        quick_sort(0, len(nums) - 1)
        return nums

