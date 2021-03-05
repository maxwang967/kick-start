class Solution:
    def mySqrt(self, x: int) -> int:
        # 1 calculator
        # if x == 0:
        #     return 0
        # result = int(exp(0.5 * log(x)))
        # return result + 1 if (result + 1) ** 2 <= x else result
        # 2 binary search
        left = 0
        right = x
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
        

          
