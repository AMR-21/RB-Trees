from Dic import Dictionary as d

d1 = d('W:\Projects\Data Structures II\RB-Trees\EN-US-Dictionary.txt')

def printSize():
    size = d1.tree.size(d1.tree.root)
    height = d1.tree.height(d1.tree.root)
    print('''Current dictionary size is {}
Current Red-Black tree height is {}\n'''.format(size, height))

func = None
menu = '''
Menu:
=====
1. Load
2. Insert word
3. Look-up word
4. Exit'''

print(menu)
while func != 'exit':
    try:
        f = int(input('Choose a function: '))
    except:
        print('Not a number')
        continue
    if f == 1:
        d1.load()
        printSize()
    elif f == 2:
        word = input('Enter the word: ')
        word += '\n'
        print(d1.insert(word))
        printSize()
    elif f == 3:
        word = input('Enter the word: ')
        word += '\n'
        if d1.lookUP(word):
            print('Yes, {} exists\n'.format(word.strip()))
        else:
            print('No, {} does not exist\n'.format(word.strip()))             
    elif f == 4:
        func = 'exit'
    else:
        print ('Wrong input')    
    