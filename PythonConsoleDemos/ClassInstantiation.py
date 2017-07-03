#Demonstrate class instantiation
import BasicClass as bc
import DerivedClass as dc

def main():
    basicclass = bc.BasicClass()
    numOut = basicclass.method1(5.7)
    print('number out is {}\n'.format(numOut))

    print('Now test derived class')

    derivedclass = dc.DerivedClass()
    numOutDerived = derivedclass.methodDerived(8.734)
    print('derived class number out is {}\n'.format(numOutDerived))
    derivedclass.method1(5.7)


    raw_input('press enter to finish')

if __name__ == '__main__':
    main()
