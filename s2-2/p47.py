import numpy as np

class LinePoint():
    def __init__(self, X, R):
        self.X = X
        self.R = R
    
    def searchpoint(self, top):
        top_elem = self.X[top]
        for i in range(top, self.N):
            if(self.X[i] - top_elem > self.R):
                return i - 1
    
    def reachpoint(self, point):
        pointelem = self.X[point]
        for i in range(point, self.N):
            if(self.X[i] - pointelem > self.R):
                return i
        return -1

    def solve(self):
        self.N = self.X.size
        pointnum = 0

        ind = 0
        while True:
            #print("ind", ind)
            ind = self.searchpoint(ind)
            #print("point", ind)
            pointnum += 1
            ind = self.reachpoint(ind)
            if(ind < 0):
                break
            elif(ind == self.N-1):
                pointnum += 1
                break
            #print("reach", ind)
        
        print(pointnum)

if __name__ == '__main__':
    X = np.array([1, 7, 15, 20, 30, 60])
    R = 10
    linepoint = LinePoint(X, R)
    linepoint.solve()