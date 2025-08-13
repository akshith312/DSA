class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(n):
            for c in range(n):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])

        return True
        