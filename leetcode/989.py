class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        K_array = [int(x) for x in str(K)]
        K_n = len(K_array)
        A_n = len(A)
        carry = 0
        border = min(A_n, K_n)
        for i in range(border):
            cur_K = K_n - 1 - i
            cur_A = A_n - 1 - i
            add_K = K_array[cur_K]
            add_A = A[cur_A]
            s = add_A + add_K + carry
            carry = s // 10
            dig = s % 10
            result.append(dig)
        if A_n == K_n and carry == 1:
            result.append(carry)
        elif border == A_n:
            for i in range(border, K_n):
                cur_K = K_n - 1 - i
                add_K = K_array[cur_K]
                s = add_K + carry
                carry = s // 10
                dig = s % 10
                result.append(dig)
                if i == K_n - 1 and carry == 1:
                    result.append(carry)
        elif border == K_n:
            for i in range(border, A_n):
                cur_A = A_n - 1 - i
                add_A = A[cur_A]
                s = add_A + carry
                carry = s // 10
                dig = s % 10
                result.append(dig)
                if i == A_n - 1 and carry == 1:
                    result.append(carry)


        return result[::-1]
            