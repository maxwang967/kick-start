class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        def equal(x, y):
            if x > 0 and x - y <= 1e-5:
                return True
            if x < 0 and y - x >= 1e5:
                return True
            return False
        def p(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            result = p(x, n >> 1)
            result *= result
            if n & 1 == 1:
                result *= x
            return result
        
        if equal(x, 0.0) and n < 0:
            return 0
        
        result = p(x, abs(n))
        if n < 0:
            result = 1.0 / result
        return result
        