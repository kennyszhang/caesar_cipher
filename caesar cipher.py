#caesar cipher by kenny zhang
import enchant
import random

def cipher():
    inp = input('\nenter message: ')
    inp = inp.lower()
    while True:
        shift = input('\nenter integer amount to shift\ninput "r" to generate random integer: ')
        if (shift == 'r'):
            shift = int(random.randint(1,25))
            break
        else:
            print('\ninvalid input')
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

def decipher():
    d = enchant.Dict("en_US")
    inp = input('\nenter message: ')
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
        print('output: no output was found\n\nexecuting bruce force attack')
        table = ('\n\nshift    output')
        print(table)
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
            if (x+1) <= 9:
                print(str(x+1), '      ', result)
            else:
                print(str(x+1), '     ', result)
            result = ''
    print('\n\n')
    main()

def sample():
    print('\n\ninput:  the quick brown fox jumps over the lazy dog.')
    print('output: aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.')
    print('shift:  7\n\n\n')
    main()

def main():
    menu = 'caesar cipher menu'
    print(menu)
    print('-'*len(menu))
    print('[1] cipher\n[2] decipher\n[3] sample\n[4] quit')
    option = input('\nenter menu option and ENTER: ')
    if option == '1':
        cipher()
    elif option == '2':
        decipher()
    elif option == '3':
        sample()
    else:
        quit()

if __name__ == "__main__":   
    main()

