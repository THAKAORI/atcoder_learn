import numpy as np

class Schedule():
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def solve(self):
        self.now = 0
        work = 0
        max_time = np.max(self.t)

        while True:
            self.now = np.min(self.t[self.s > self.now])
            work += 1
            if(self.now >= max_time):
                break

        print(work)


if __name__ == '__main__':
    s = np.array([1, 2, 4, 6, 8])
    t = np.array([3, 5, 7, 9, 10])

    schedule = Schedule(s, t)
    schedule.solve()