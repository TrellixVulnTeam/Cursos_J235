import math


def dividing(list_in, div):
    #defensive programation
    try:
        return [i / div for i in list_in]

    #ZeroDivisionError is the error that appears
    #when running the program and dividing by zero
    #Once we write that we except this situation.
    #we're controlling our code over the possible mistakes
    #made by a user.
    except ZeroDivisionError as error0:
        print(error0)
        return list_in


def neg_root(list_in, div):
    try:
        return [math.sqrt(i) for i in list_in]
    except ValueError:
        print("This program is not meant to print imaginary numbers")
        return 0


def main():
    list_in = list(range(-10, 0))
    div = int(input('Type a number: '))
    print(list_in)

    print(neg_root(list_in, div))


if __name__ == '__main__':
    main()
