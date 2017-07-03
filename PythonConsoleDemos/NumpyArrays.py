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

    #reshape an array
    print('reshape an array')
    aone = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    print('original: {}'.format(aone))
    a22 = aone.reshape((3,4))
    print('reshaped. Notice the row ordering: \n{}'.format(a22))
    print('\n')
    print('reshape back to row vector:\n{}'.format(a22.reshape((1,12))))
    print('\n')

    #access a range of elements
    print('show elements 0,1, and 2')
    asub = aone[0:3]
    print('first three elements: \n{}'.format(asub))
    print('\n')

    #get the length of an array
    print('length of aone is:\n{}'.format(len(aone)))

    #access last three elements
    print('show last three elements')
    print('last three elements:\n{}'.format(aone[len(aone)-3:]))
    #asubend = aone()








    raw_input('press enter to finish')

if __name__ == '__main__':
    main()
