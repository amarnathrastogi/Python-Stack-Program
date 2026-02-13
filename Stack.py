Stack = []

def push():
    value = int(input('\nEnter Element What You Want To Add... '))
    Stack.append(value)
    print('\nElement Pushed In Stack Sucessfully.',value)

def pop():
    if len(Stack) == 0 :
        print('\nStack Is Empty.')
    else :
         value =  Stack.pop()
         print('\nElement Poped In Stack Sucessfully.',value)

def display():
    print(Stack)


while True :

    print('----------------------------------------')
    print('\n1. To Push The Value...')
    print('2. To Pop The Value...')
    print('3. To Display The Elements...')
    print('4. Exit.')

    Choice = int(input('Enter , What Do You Want : '))

    if Choice == 1:
        push()
    elif Choice == 2:
        pop()
    elif Choice == 3:
        display()
    elif Choice == 4:
        break
    else :
        print('\nInvalid Choice.')
