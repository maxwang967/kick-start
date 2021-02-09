class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 0:
            return 0
        result = 1
        left = 0
        right = 0
        while right < l - 1:
            if left == right:
                if arr[right] == arr[right + 1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                elif arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                else:
                    left = right
            result = max(result, right - left + 1)
            
        return result