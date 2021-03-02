class Solution:
    def partition(self, nums, lo, hi):
        if lo == hi:
            return lo
        i = lo + 1
        j = hi
        pivot = nums[lo]
        while True:
            while nums[i] <= pivot:
                if i == hi:
                    break
                i += 1
            while nums[j] >= pivot:
                if j == lo:
                    break
                j -= 1

            if i >= j:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]

        return j


    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0 or k == 0:
            return []
        lo = 0
        hi = n - 1
        while lo <= hi:
            p = self.partition(arr, lo, hi)
            if p < k - 1:
               lo = p + 1
            elif p > k - 1:
                hi = p - 1
            else:
                return arr[:p + 1]
        return []
