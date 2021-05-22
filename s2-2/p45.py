import numpy as np
from copy import *

from numpy.lib.function_base import select

class WordLine():
    def __init__(self, S):
        self.S = S
        self.S = np.array(list(self.S))
    
    def select(self, input):
        if(input.size == 1):
            return True
        first = input[0]
        last = input[-1]
        if(first == last):
            return self.select(input[1:-1])
        elif first < last:
            return True
        else:
            return False
            

    def solve(self):
        sentence = deepcopy(self.S)
        result = list()

        while(sentence.size != 0):
            compare = self.select(sentence)
            if(compare):
                temp = sentence[0]
                sentence = np.delete(sentence, 0)
            else:
                temp = sentence[-1]
                sentence = np.delete(sentence, -1)
            result.append(temp)
        print(self.S)
        print(result)


if __name__ == '__main__':
    S = "ACDBCB"
    wordline = WordLine(S)
    wordline.solve()
