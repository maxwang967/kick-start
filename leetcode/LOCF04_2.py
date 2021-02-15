# 题目：
# 有两个排序的数组A1和A2，内存在A1的末尾有足够的空余空间容纳A2。
# 请写一个函数，把A2的所有数字插入A1中，并且所有的数字是排序的。

A_1 = [1, 2, 4, 0, 0 , 0, 0, 0]
A_2 = [1, 2, 3, 7, 8]

class Solution:
    def __init__(self) -> None:
        pass
    
    def merge(self, A_1, A_2, len_A, len_B):
        len_A_all = len(A_1)
        p_1 = len_A - 1
        p_2 = len_B - 1
        p_new = len_A_all - 1
        while p_1 >= 0 and p_2 >= 0:
            if A_1[p_1] > A_2[p_2]:
                A_1[p_new] = A_1[p_1]
                p_1 -= 1
            else:
                A_1[p_new] = A_2[p_2]
                p_2 -= 1
            p_new -= 1
        while p_1 >= 0:
            A_1[p_new] = A_1[p_1]
            p_new -= 1
            p_1 -= 1
        while p_2 >= 0:
            A_2[p_new] = A_2[p_1]
            p_new -= 1
            p_2 -= 1
        return A_1
        


sl = Solution()
print(sl.merge(A_1, A_2, 3, 5))