class Game:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.amount = 4  # how many in a row

        self.p = 1  # whose turn
        self.col = 0  # current column chosen
        self.w = 0  # continue 0 /win 2/draw 1
        self.l = [([0] * self.rows) for i in range(self.cols)]  # empty matrix of grid
        self.g = 1  # which game/round

    def nextp(self):
        self.p = int(2 / self.p)

    def add(self):
        for item in self.l[self.col]:
            if item == 0:
                self.l[self.col][self.l[self.col].index(0)] = self.p
                break

    def restart(self):
        self.w = 0
        self.l = [([0] * self.rows) for i in range(self.cols)]
        self.g += 1
        self.p = (self.g + 1) % 2 + 1  # alternate turns

    def check(self):

        lst = [i for i in self.l[self.col] if i != 0]  # remove zeros at end
        x, y = self.col, len(lst) - 1  # coordinate of last piece placed

        def diagonal(cols, rows, l, am, x, y):
            # downward diagonal
            dcol = [[x, y]]  # list of diagonal

            a, b = x, y
            while True:
                a = a + 1
                b = b - 1
                if a == cols or b == -1:
                    break
                dcol.append([a, b])

            a, b = x, y
            while True:
                a = a - 1
                b = b + 1
                if a == -1 or b == rows:
                    break
                dcol.append([a, b])

            dcol = sorted(dcol, key=lambda x: x[0])
            for i in range(len(dcol) + 1 - am):
                r = []
                for j in range(am):
                    r.append(l[dcol[i + j][0]][dcol[i + j][1]])  # list of 4 spots
                if (
                    len(set(r)) == 1 and list(set(r))[0] != 0
                ):  # check if list of 4 is the same
                    return True

            # upwards diagonal
            ucol = [[x, y]]  # list of diagonal

            a, b = x, y
            while True:  # forwards/upwards
                a = a + 1
                b = b + 1
                if a == cols or b == rows:
                    break
                ucol.append([a, b])

            a, b = x, y
            while True:  # backwards/downwards
                a = a - 1
                b = b - 1
                if a == -1 or b == -1:  # out of bounds
                    break
                ucol.append([a, b])

            ucol = sorted(ucol, key=lambda x: x[0])  # ascending order
            for i in range(
                len(ucol) + 1 - am
            ):  # possible combinations for 'am' in a row in diagonal
                r = []
                for j in range(am):
                    r.append(l[ucol[i + j][0]][ucol[i + j][1]])
                if (
                    len(set(r)) == 1 and list(set(r))[0] != 0
                ):  # check if list of 4 is the same
                    return True

            return False

        def row(l, cols, lst, am):
            h = len(lst) - 1  # row to check
            for i in range(
                1, cols + 2 - am
            ):  # for n col, only 'am' placements. indexing backwards so 1:'am'+1
                r = []
                for j in range(am):
                    r.append(l[-i - j][h])  # list of 4 spots being checked
                if (
                    len(set(r)) == 1 and list(set(r))[0] != 0
                ):  # check if list of 4 is the same
                    return True

            return False

        def column(lst, am):
            if len(lst) > am - 1:  # if length is am or bigger
                if (len(set(lst[-am:]))) == 1:  # if last 4 piecs the same
                    return True

            return False

        if (
            row(self.l, self.cols, lst, self.amount)
            or column(lst, self.amount)
            or diagonal(self.cols, self.rows, self.l, self.amount, x, y)
        ):
            self.w = 2

        elif all(cl[-1] != 0 for cl in self.l):  # if full and no winner
            self.w = 1
