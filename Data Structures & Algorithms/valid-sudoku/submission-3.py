class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horz lines 
        for line in board:
            seen = set()

            for tile in line:
                if tile == ".":
                    continue
                if tile in seen:
                    print("Failed Row Check")
                    return False
                seen.add(tile)

        col = 0
        for i in range(len(board)):
            seen = set()
            while col < len(board):
                print(f"col check on :", i, col)
                if board[col][i] in seen:
                    print("Failed Col Check")
                    return False
                if board[col][i] != ".":
                    seen.add(board[col][i])

                col += 1

            col = 0


        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                seen = set()
                row, col = i, j 
                for x in range(3):
                    for y in range(3):
                        if board[row+x][col+y] in seen:
                            print("Failed Cube Check")
                            return False
                        if board[row+x][col+y] != ".":
                            seen.add(board[row+x][col+y])

        return True
