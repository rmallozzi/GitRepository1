#Demo of various output formatting

def main():

    print
    #Trimming output precision of a number
    pi = 3.14159265359
    print('with no trimming {}\n'.format(pi))

    #Trim to 2 decimals
    print('Trimmed to 2 decimal places {:.2f}\n'.format(pi))

    #Multiple numbers in a line
    num1 = 1.23456
    num2 = 2.3456789
    print('num1 and num2 are {:.2f} and {:.3f}\n'.format(num1,num2))

    #concatenating strings
    str1 = 'The cat '
    str2 = 'jumped over the moon'
    print(str1+str2+'\n')



    raw_input('press enter to finish')

if __name__ == '__main__':
    main()
