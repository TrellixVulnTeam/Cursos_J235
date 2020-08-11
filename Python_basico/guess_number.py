import random
import math


def guess_number(random_number):
    user_option = int(input('Tip a number please: '))

    if user_option < random_number:
        print('Try with a higher number!')
        return False
    elif user_option > random_number:
        print('Try with a lower number!')
        return False
    else:
        print('You won!')
        return True


def main():
    #Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    test = """
    Yo la verdad no sé si los
    saltos de línea se respetan
    a la hora de imprimir
    """

    print(test)
    
    lifes = 6

    while guess_number(random_number) == False:
        lifes -= 1
        guess_number(random_number)
        print(lifes)
        if lifes < 0:
            print('You\'ve lost!')
            break


if __name__ == '__main__':
    main()
