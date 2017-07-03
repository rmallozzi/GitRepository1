#Demonstration of derived class
import BasicClass as bc

class DerivedClass(bc.BasicClass):

    def __init__(self):
        bc.BasicClass.__init__(self)
        print('derived constructor entered')


    def methodDerived(self,numIn):
        print('Number entered to methodDerive is {}\n'.format(numIn))
        numOut = numIn+2;
        print('methodDerived output number is {}\n'.format(numOut))

        return(numOut)

    def method1(self,numIn):
        print('override method1 called in derived class with input value {}'.format(numIn))
        numOut = numIn+4
        print('input value + 4 is {}'.format(numOut))
        return(numOut)