import numpy as np


class Spielfeld:
    def __init__(self, arr=None):
        self.score = 0
        if arr == None or arr != numpy.ndarray:
            self.field = np.zeros((4, 4), int)
        else:
            if len(arr.shape) != 2:
                self.field = np.zeros((4, 4), int)
            else:
                self.field = arr

        self.dims = self.field.shape

        self.add_numbers()
        self.add_numbers()

    def __repr__(self):
        r = "--------------\n"

        for i in range(4):
            r += "| "
            for j in range(4):
                if self.field[i, j] == 0:
                    pass
                else:
                    r += str(self.field[i, j])
                r += " | "
            r += "\n"
        r += "--------------\n"

        return r

    def add_numbers(self):
        freefields = []
        for i, field in enumerate(self.field.flat):
            if field == 0:
                freefields.append(i)

        ind = freefields[np.random.randint(len(freefields))]

        if np.random.randint(2) == 0:
            self.field[ind // self.dims[1], ind % self.dims[1]] = 2
        else:
            self.field[ind // self.dims[1], ind % self.dims[1]] = 4

    def line_movable(self, arr, merged):
        for i, elem in enumerate(arr):
            if (
                elem != 0
                and i != 0
                and (
                    arr[i - 1] == 0
                    or (arr[i - 1] == elem and i - 1 not in merged and i not in merged)
                )
            ):
                return True
        return False

    def lines_movable(self, direction, merged):
        if direction == "up":
            for i in range(self.field.shape[1]):
                if self.line_movable(self.field[:, i], merged[i]):
                    return True
            return False
        elif direction == "down":
            for i in range(self.field.shape[1]):
                if self.line_movable(self.field[::-1, i], merged[i]):
                    return True
            return False
        elif direction == "left":
            for i in range(self.field.shape[0]):
                if self.line_movable(self.field[i, :], merged[i]):
                    return True
            return False
        else:
            for i in range(self.field.shape[0]):
                if self.line_movable(self.field[i, ::-1], merged[i]):
                    return True
            return False

    def gameover(self, merged):
        for direction in ["up", "down", "left", "right"]:
            if self.lines_movable(direction, merged):
                return False
        return True

    def win(self):
        return 2048 in self.field

    def rowmove(self, arr, merged, score, factor):
        for i in range(arr.size - 1):
            if arr[i] == 0 and arr[i + 1] != 0:
                arr[i] = arr[i + 1]
                arr[i + 1] = 0
            elif (
                arr[i] != 0
                and arr[i] == arr[i + 1]
                and i not in merged
                and i + 1 not in merged
            ):
                factor += 1
                score += arr[i]
                arr[i] += arr[i + 1]
                arr[i + 1] = 0
                merged.append(i)
        return score, factor

    def single_step(self, direction, merged, score, factor):
        if direction == "up":
            for i in range(self.field.shape[1]):
                score, factor = self.rowmove(self.field[:, i], merged[i], score, factor)
        elif direction == "down":
            for i in range(self.field.shape[1]):
                score, factor = self.rowmove(
                    self.field[::-1, i], merged[i], score, factor
                )
        elif direction == "left":
            for i in range(self.field.shape[0]):
                score, factor = self.rowmove(self.field[i, :], merged[i], score, factor)
        else:
            for i in range(self.field.shape[0]):
                score, factor = self.rowmove(
                    self.field[i, ::-1], merged[i], score, factor
                )
        return score, factor

    def full_move(self, direction):
        merged = [[] for i in range(4)]
        tempscore = 0
        factor = 0
        if self.lines_movable(direction, merged):
            while self.lines_movable(direction, merged):
                tempscore, factor = self.single_step(direction, merged)
            self.add_numbers()
        self.score += factor * tempscore


def main(*args):
    pass
