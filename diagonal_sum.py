from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum_value = 0

        for i in range(n):

            sum_value += mat[i][i] + mat[n - 1 - i][i]

        if n % 2:
            sum_value -= mat[n // 2][n // 2]

        return sum_value


solution = Solution()
solution.diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
