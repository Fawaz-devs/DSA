class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n  = len(matrix), len(matrix[0])

        L, R = 0 , m*n -1

        while L<= R :
            mid = (L+R ) // 2
            i, j = mid // n , mid% n

            if matrix[i][j] < target : 
                L  = mid + 1
            elif matrix[i][j] > target :
                R = mid -1

            elif matrix[i][j] == target :
                return True
        return False 
            