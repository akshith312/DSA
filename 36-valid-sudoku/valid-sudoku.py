class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #brute force
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i]=='.':
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[i][col]=='.':
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])
        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square // 3) * 3 + i
        #             col = (square % 3) * 3 + j

        #             if board[row][col] == '.':
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
        