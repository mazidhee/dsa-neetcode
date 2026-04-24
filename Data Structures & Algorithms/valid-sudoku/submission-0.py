import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        co = collections.defaultdict(set) #hashset
        ro = collections.defaultdict(set)
        squ = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                 if board[r][c] == ".": #checking if empty
                    continue
                 if ( board[r][c] in ro[r]
                    or board[r][c] in co[c]
                    or board[r][c] in squ[(r // 3, c // 3)]):
                    return False

                 co[c].add(board[r][c])
                 ro[r].add(board[r][c])
                 squ[(r // 3, c // 3)].add(board[r][c])

        return True

        