class CIslandCounter:
    def __init__(self, binaryMatrix):
        self.M = binaryMatrix
        from collections import namedtuple
        self.pair = namedtuple("pair", ["first", "second"])

    def getIslands(self):
        islands = 0
        for i in range(self.rows()):
            for j in range(self.cols()):
                if self.M[i][j] > 0:
                    self.__markIslands(self.rows(), self.cols(), i, j)
                    islands += 1
        return islands

    def rows(self):
        return len(self.M)

    def cols(self):
        return len(self.M[0])

    def __markIslands(self, rows, cols, i, j):
        q = []
        q.append(self.pair(i, j))
        while len(q) > 0:
            item = q.pop(0)
            x = item.first
            y = item.second
            if self.M[x][y] == 1:
                self.M[x][y] = -1
                self.__pushIfValid(q, rows, cols, x - 1, y - 1)
                self.__pushIfValid(q, rows, cols, x - 1, y)
                self.__pushIfValid(q, rows, cols, x - 1, y + 1)
                self.__pushIfValid(q, rows, cols, x, y - 1)
                self.__pushIfValid(q, rows, cols, x, y + 1)
                self.__pushIfValid(q, rows, cols, x + 1, y - 1)
                self.__pushIfValid(q, rows, cols, x + 1, y)
                self.__pushIfValid(q, rows, cols, x + 1, y + 1)

    def __pushIfValid(self, q, rows, cols, x, y):
        if x >= 0 and x < rows and y >= 0 and y < cols:
            q.append(self.pair(x, y))


if __name__ == "__main__":
    M = [[1, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 0]]

    c = CIslandCounter(M)

    for i in range(c.rows()+2):
        for j in range(c.cols()+2):
            print(("\033[1;31m█\033[0m" if M[i-1][j-1] else "░") if (i-1 >= 0 and i-1<c.rows() and j-1>=0 and j-1<c.cols()) else ("▓" if j-1<c.cols() else "▓\n"), end = '')

    print(f"\nNumber of islands is: {c.getIslands()}\n")
