w = 10
n = 4
val = [10, 40, 30, 50]
wt = [5, 4, 6, 3]
mat = [[0 for _ in range(w + 1)] for _ in range(n + 1)]


def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]

for item in range(1, n + 1):
    for capacity in range(1, w + 1):
        val_without_current = mat[item - 1][capacity]
        val_with_current = 0
        w_current = wt[item - 1]
        if capacity >= w_current:
            val_with_current = val[item - 1]
            remaining_cap = capacity - w_current
            val_with_current += mat[item - 1][remaining_cap]
        mat[item][capacity] = max(val_with_current, val_without_current)
print(mat[n][w])
# print(knapSack(w, wt, val, n))
