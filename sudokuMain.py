class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __str__(self):
        return " - "

class FilledSquare(Square):
    def __init__(self, row, column, value, stone):
        super().__init__(row, column)
        self.value = value
        self.stone = stone #whether the value is "set in stone"
    def __str__(self):
        return " " + str(self.value) + ("*" if self.stone else " ")

class Board:
    def __init__(self, start=[]): # start is a list of preset Filled Squares
        self.board = []
        for r in range(9):
            self.board.append([])
            for c in range(9):
                self.board[r].append(Square(r, c))
        for square in start:
            self.add_square(square)

    def add_square(self, square):
        self.board[square.row][square.column] = square

    def check_win(self):
        for row in self.board:
            bingo = [False]*9 #keeps track of whether each number has appeared in a given set. index i tracks number i+1
            for square in row:
                if not isinstance(square, FilledSquare):
                    return False
                bingo[square.value - 1] = True
            if bingo != [True]*9:
                return False
        print("rows good")
        for col in range(9):
            bingo = [False] * 9
            for row in self.board:
                bingo[row[col].value - 1] = True
            if bingo != [True]*9:
                return False
        print("cols good")
        for third in range(3):
            for chunk in range(3):
                bingo = [False]*9
                for r in range(third*3, third*3+3):
                    for c in range(chunk*3, chunk*3+3):
                        bingo[self.board[r][c].value - 1] = True
                if bingo != [True]*9:
                    return False
        print("chunks good")
        return True

    def __str__(self):
        str = ""
        for row in self.board:
            for square in row:
                str += square.__str__() + " "
            str += "\n"
        return str

empt = Square(0, 0)
print(empt)

phil = FilledSquare(0, 1, 9, True)
print(phil)

#this code sets up a list of squares for a solved grid, to test the check_win
solved = "435269781682571493197834562826195347374682915951743628519326874248957136763418259"
solvedList = []
sRow = 0
sCol = 0
while solved != "":
    solvedList.append(FilledSquare(sRow, sCol, int(solved[0]), False))
    solved = solved[1:]
    sCol += 1
    if sCol == 9:
        sRow += 1
        sCol = 0

b = Board([phil])
print(b)
print(b.check_win())

s = Board(solvedList)
print(s)
print(s.check_win())