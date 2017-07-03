#Demo of numpy arrays

import numpy as np

def main():

    #one-dimensional array
    print('\nOne-dimensional array')
    a1 = np.array([1.1,2.3,3.3,4.4])
    print(a1)
    print('\n')

    #two-dimensional array
    print('two-dimensional array')
    a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(a2)
    print('\n')

    #allocating array of zeros
    print('array of zeros')
    a0 = np.zeros((2,3))
    print(a0)
    print('\n')

    #three-dimensional array
    print('three-dimensional array')
    a3 = np.array([[ [1,2,3],[4,5,6],[7,8,9] ],
                   [ [10,11,12],[13,14,15],[16,17,18] ],
                   [ [19,20,21],[22,23,24],[25,26,27]] ])

    print(a3)
    print('\n')



    raw_input('press enter to finish')

if __name__ == '__main__':
    main()
