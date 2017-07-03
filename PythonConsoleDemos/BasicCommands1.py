

def main():

    #print the numbers 1 through 5
    for i in range(1,6):
        print(i)

    #print a newline
    print('\n')

    #use an if statement
    for i in range(5):
        if i == 3:
            print(i)
            print('found it!')
        else:
            print('not the selected digit')


    #use a while statement
    print
    print('While statement demo')
    ind = 0
    while(ind < 5):
        print(ind)
        ind = ind+1


    #keep box open until user enters
    raw_input('push enter to finish')


if __name__ == '__main__':
    main()
