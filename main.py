class Board:
    def __init__(self, ):
        self.N = 3
        self.CIRCLE = 1
        self.CROSS = -1
        self.EMPTY = 0
        self.board = [[self.EMPTY]*self.N for i in range(self.N)]

    def get_opposite_player(self, player):
        if player == self.CIRCLE:   return self.CROSS
        if player == self.CROSS:    return self.CIRCLE
        return self.EMPTY

    def print_board(self, ):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == self.CIRCLE: print("o", end=" ")
                if self.board[i][j] == self.CROSS: print("x", end=" ")
                if self.board[i][j] == self.EMPTY: print(".", end=" ")
            print()
    

    def checkWinner(self, ):
        """
        return [isFinish(boolean), winner(int)]
        """
        for player in [self.CIRCLE, self.CROSS]:
            for i  in range(self.N):
                tmp = True
                for j in range(self.N):
                    if player != self.board[i][j]:
                        tmp = False
                if tmp:
                    return [True, player]
        for player in [self.CIRCLE, self.CROSS]:
            for i  in range(self.N):
                tmp = True
                for j in range(self.N):
                    if player != self.board[j][i]:
                        tmp = False
                if tmp:
                    return [True, player]
        for player in [self.CIRCLE, self.CROSS]:
            tmp = True
            for i  in range(self.N):
                if player != self.board[i][i]:
                    tmp = False
            if tmp:
                return [True, player]
        
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == self.EMPTY:
                    return [False, self.EMPTY]
        return [True, self.EMPTY]
    
    def put(self, row, col, value):
        self.board[row][col] = value
    
    def read_input(self, ):
        while True:
            string = input()
            if not string.replace(" ", "").isdecimal():
                continue
            if len(string.split()) != 2:
                continue
            row, col = map(int, string.split())
            if 0<=row<self.N and 0<=col<self.N and self.board[row][col] == self.EMPTY:
                return row, col

    
    def loop(self, ):
        player = self.CIRCLE
        while True:
            isFinish, winner = self.checkWinner()
            if isFinish:
                if winner == self.CIRCLE:   print("winner: o")
                if winner == self.CROSS:   print("winner: x")
                if winner == self.EMPTY:   print("draw")
                return
            self.print_board()
            row, col = self.read_input()
            self.put(row, col, player)
            player = self.get_opposite_player(player)


def main():
    board = Board()
    board.loop()


if __name__=="__main__":
    main()