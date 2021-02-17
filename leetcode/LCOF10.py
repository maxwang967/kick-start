class Solution:
    def fib(self, n: int) -> int:
        # 1 recursive
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)
        # 2 iteration
        f_01 = [0, 1]
        if n < 2:
            return f_01[n]
        f_n = 0
        f_n1 = f_01[0]
        f_n2 = f_01[1]
        for i in range(n - 1):
            f_n = f_n1 + f_n2
            f_n1 = f_n2
            f_n2 = f_n
        return f_n % 1000000007