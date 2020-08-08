import sys
import math
import time

class Complexities:

    def __init__(self, n):
        self.n = n

    def constant(self):
        return 1

    def linear(self):
        return self.n

    def logarithm(self):
        return math.log10(self.n)

    def llogarithm(self):
        return self.n * math.log10(self.n)

    def polinomial(self):
        return self.n ** 2

    def exponential(self):
        return 2 ** self.n


def main():

    sys.setrecursionlimit(500000)
    number = [10, 100, 1000]

    print('_____________________________________________')
    for n in number:

        print('------------ Starts test for {} ------------\n \n'.format(n))

        complexity = Complexities(n)
        start = time.time()
        #print(start)
        print('Constant complexity for {} is'.format(n),complexity.constant())
        finish = time.time()
        print('Runtime',finish - start)
        #print(finish)
        print('_____________________________________________')

        start = time.time()
        print('Linear complexity for {} is'.format(n),complexity.linear())
        finish = time.time()
        print('Runtime',finish - start)
        print('_____________________________________________')

        start = time.time()
        print('Logarithm complexity for {} is'.format(n),complexity.logarithm())
        finish = time.time()
        print('Runtime',finish - start)
        print('_____________________________________________')

        start = time.time()
        print('Linear logarithm complexity for {} is'.format(n),complexity.llogarithm())
        finish = time.time()
        print('Runtime',finish - start)
        print('_____________________________________________')

        start = time.time()
        print('Polinomial complexity for {} is'.format(n),complexity.polinomial())
        finish = time.time()
        print('Runtime',finish - start)
        print('_____________________________________________')

        start = time.time()
        print('Exponential complexity for {} is'.format(n),complexity.exponential())
        finish = time.time()
        print('Runtime',finish - start)
        print('\n \n************ Finish test for {} ************\n \n'.format(n))



if __name__ == '__main__':
    main()
