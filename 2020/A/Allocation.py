import sys

"""
Problem
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.

Limits
Time limit: 15 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ Ai ≤ 1000, for all i.

Test set 1
1 ≤ N ≤ 100.

Test set 2
1 ≤ N ≤ 105.

Sample

Input

Output
 
3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999

  
Case #1: 2
Case #2: 3
Case #3: 0

  
In Sample Case #1, you have a budget of 100 dollars. You can buy the 1st and 3rd houses for 20 + 40 = 60 dollars.
In Sample Case #2, you have a budget of 50 dollars. You can buy the 1st, 3rd and 4th houses for 30 + 10 + 10 = 50 dollars.
In Sample Case #3, you have a budget of 300 dollars. You cannot buy any houses (so the answer is 0).
"""

T = input()
for idx in range(int(T)):
    sys.stdout.flush()
    N, B = map(int, input().split())
    sys.stdout.flush()
    costs = map(int, input().split())
    costs = sorted(costs)
    max_number = 0
    for cost in costs:
        if B - cost < 0:
            break
        B = B - cost
        max_number += 1
    print("Case #{0}: {1}".format(idx + 1, max_number))