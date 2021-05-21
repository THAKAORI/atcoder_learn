import numpy as np
import queue


mase = np.array(["#S######.#", 
                "......#..#",
                ".#.##.##.#",
                ".#........",
                "##.##.####",
                "....#....#",
                ".#######.#",
                "....#.....",
                ".####.###.",
                "....#...G#"])
class MaseSolve:
    def thisposvalide(self, y, x):
        if y >= 0 and x >= 0 and y < self.masemap.shape[0] and x < self.masemap.shape[1]:
            if self.masemap[y, x] == "." and self.searched[y, x] == 0:
                return 1
            elif self.masemap[y, x] == "G":
                return 2
        
        return 0

    def reachablepos(self):
        y, x, path = self.pos.get()
        print(y, x, path)

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        move_path = path + 1
        for move in moves:
            temp_y = y + move[0]
            temp_x = x + move[1]

            valid = self.thisposvalide(temp_y, temp_x)
            if valid == 2:
                return move_path
            elif valid == 1:
                self.pos.put([temp_y, temp_x, move_path])
                self.searched[temp_y, temp_x] = 1
        
        return 0


    def solvemasepath(self, mase):
        self.masemap = np.array([np.array(list(row)) for row in mase])

        n, m = self.masemap.shape
        self.searched = np.zeros((n, m))
        start = np.where(self.masemap == "S")

        self.pos = queue.Queue()
        self.pos.put([start[0][0], start[1][0], 0])
        self.searched[start[0][0], start[1][0]] = 1

        goal = False
        while(goal == 0):
            goal = self.reachablepos()
        
        print(goal)

    




if __name__ == '__main__':
    masesolve = MaseSolve()
    masesolve.solvemasepath(mase)



    