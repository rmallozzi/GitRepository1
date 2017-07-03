#Demo of basic numpy usage
import numpy as np
import math #not needed for numpy, just for comparison in demo

def main():
    a1 = 3

    #use numpy cos function
    print('numpy cosine {:.5f}'.format(np.cos(a1)))

    #use regular python built-in cosine
    print('python built-in cosine: {:.5f}'.format(math.cos(a1)))

    #creating a range progression
    print('basic range with unit step size')
    a2 = np.arange(1,5)
    print(a2)

    #range with set step
    print('range with 0.2 step intervals')
    a3 = np.arange(1,3,0.2)
    print(a3)


    raw_input('press enter to finish')

if __name__ == '__main__':
    main()
