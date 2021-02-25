class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for j in range(cols):
            result.append([])
            # print(f"j={j}")
            for i in range(rows):
                # print(f"{i},{j}")
                # print(matrix[i][j])
                result[j].append(matrix[i][j])

        
        return result