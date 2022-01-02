#caesar cipher 2 by kenny zhang
import enchant
import random

def main():
    menu = 'caesar cipher menu'
    print(menu)
    print('-'*len(menu))
    print('[1] cipher a message\n[2] decipher a message\n[3] quit')
    option = input('\nenter a menu option and ENTER: ')
    if option == '1':
        cipher()
    elif option == '2':
        decipher()
    else:
        quit()

#cipher
def cipher():
    inp = input('\nenter a message: ')
    inp = inp.lower()
    shift = int(input('\nenter a integer amount to shift; input "random" to generate random integer: '))
    if (shift == 'random'):
        shift = int(random.randint(1,25))
    print('\n\ninput:  ', inp)
    result = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for x in inp:
        if not x.isalpha():
            result += x
        else:
            x = int(letters.find(x) + shift)
            result += letters[int(x)%26]
    print('output: ', result)
    print('shift:  ', shift)
    print('\n\n')
    main()

#decipher
def decipher():
    d = enchant.Dict("en_US")
    inp = input('\nenter a message: ')
    inp = inp.lower()
    print('\n\ninput:  ', inp)
    result = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    temp = ''
    boo = False
    for x in range(25):
        for y in inp:
            if not y.isalpha():
                result += y
            else:
                shift = x + 1
                y = int(letters.find(y) - shift)
                if y <= 0:
                    y = 26 - abs(y)
                result += letters[int(y)%26]
                temp = result.split()
        if d.check(temp[0]) == True:
            print('output: ', result)
            print('shift:  ', str(x+1))
            boo = True
            break
        result = ''
    if boo == False:
        print('no output was found; executing bruce force attack')
        table = ('\n\nshift    output')
        print(table)
        print('-' * len(table))
        for x in range(26):
            for y in inp:
                if not y.isalpha():
                    result += y
                else:
                    shift = x + 1
                    y = int(letters.find(y) - shift)
                    if y <= 0:
                        y = 26 - abs(y)
                    result += letters[int(y)%26]
            if (x+1) <= 9:
                print(str(x+1), '      ', result)
            else:
                print(str(x+1), '     ', result)
            result = ''
    print('\n\n')
    main()

main()

