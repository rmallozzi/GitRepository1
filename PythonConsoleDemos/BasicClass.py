
class BasicClass(object):

    def __init__(self):
        var1 = 2.345
        print('Basic Class constructor called')


    def method1(self,numIn):
    #numIn is some number to show
        print('number sent in to method1 is {}\n'.format(numIn))
        return(numIn+1.0)


