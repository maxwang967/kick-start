class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return nums
        left = 0
        right = left + k - 1
        result = []
        while right < l:
            sub = nums[left: right + 1]
            sub.sort()
            # print(sub)
            l_sub = len(sub)
            if l_sub % 2 == 0:
                index_2 = l_sub // 2
                index_1 = index_2 - 1
                # print(f"index1={index_1}, index2={index_2}")
                result.append(
                    (sub[index_1] + sub[index_2]) / 2
                )
            else:
                result.append(
                    sub[l_sub // 2]
                )
            left += 1
            right += 1
        return result