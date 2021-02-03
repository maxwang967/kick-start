import bisect

class Solution:
    def find(self, a, value):
        lo = 0
        hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 1 classic
        # l = len(nums)
        # if l == 0:
        #     return []
        # if l == 1:
        #     return nums
        # left = 0
        # right = left + k - 1
        # result = []
        # while right < l:
        #     sub = nums[left: right + 1]
        #     sub.sort()
        #     # print(sub)
        #     l_sub = len(sub)
        #     if l_sub % 2 == 0:
        #         index_2 = l_sub // 2
        #         index_1 = index_2 - 1
        #         # print(f"index1={index_1}, index2={index_2}")
        #         result.append(
        #             (sub[index_1] + sub[index_2]) / 2
        #         )
        #     else:
        #         result.append(
        #             sub[l_sub // 2]
        #         )
        #     left += 1
        #     right += 1
        # return result
        # 2 bisect
        median = lambda x: (x[(len(x) - 1) // 2] + x[len(x) // 2]) / 2
        a = nums[:k]
        a.sort()
        result = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            # a.pop(bisect.bisect_left(a, i))
            # a.insert(bisect.bisect_left(a, j), j)
            a.pop(self.find(a, i))
            a.insert(self.find(a, j), j)            
            result.append(median(a))
        return result