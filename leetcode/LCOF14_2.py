class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        time_of_three = n // 3

        if n - 3 * time_of_three == 1:
            time_of_three -= 1
        
        time_of_two = (n - (3 * time_of_three)) // 2

        return (3 ** time_of_three * 2 ** time_of_two) % 1000000007

        