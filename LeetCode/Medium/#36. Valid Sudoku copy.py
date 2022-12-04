class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [[set() for i in range(3)] for j in range(3)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value != ".":

                    if value in row[i] or value in col[j] or value in box[i//3][j//3]:
                        return False
                    else:
                        row[i].add(value)
                        col[j].add(value)
                        box[i//3][j//3].add(value)

        return True