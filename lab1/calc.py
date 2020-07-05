import os
clear = lambda: os.system('clear') 

def seperator():
    print("=-==-" * 10)

def print_menu():
    seperator()
    print("\n Welcome to py calc \n")
    seperator()
    print('\n[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Simple sequence')
    print('[6] fibonacci')
    print("---------------------")
    print('[x] Close program \n')
    seperator()

def num1():
    return int(input('please input number 1: '))
def num2():
    return int(input('please input number 2: '))


def dif():
    return num1() - num2()

def mul():
    return num1() * num2()

def div():
    
    res1 = num1()
    res2 = num2()

    if(res2 != 0):
        return res1 / res2
    return "cant divide by 0"

def sum():
    numOfTerms = 1 + int(input('how many numbers are you adding? '))
    total = 0
    for x in range(1, numOfTerms):
        total += int(input('number ' + str(x) + ' '))
    return total
   
def seq():
    t1 = int(input('what is the first number in the sequence: '))
    d = int(input('what is the difference from number to number: '))
    n = int(input('what number in the the sequence do you want to know: '))
    return t1 + ( n-1 ) * d
    
def fob():
    a = 0
    b = 1

    nth = int(input('what term number do you want '))

    if(nth ==1 ):
        return 0


    for i in range(1, nth):
        c = a + b
        a = b
        b = c
    return c
    




# instructions

user_in = ''

while(True):
    print_menu()
    user_in = input("choose an option ")

    if(user_in == 'x'):
        clear()
        break

    clear()

    if(user_in == '1'):
        print("Result: " + str(  sum()  ) )
        

    elif(user_in == '2'):
        print("Result: " + str(  dif()  ) )
        

    elif(user_in == '3'):
        print("Result: " + str(  mul()  ) )
        

    elif(user_in == '4'):
        print("Result: " + str(  div()  ) )
        
    elif(user_in == '5'):
        print("Result: " + str(  seq()  ) )

    elif(user_in == '6'):
        print("Result: " + str(  fob()  ) )



    input('Press enter to continue...')
    clear()
