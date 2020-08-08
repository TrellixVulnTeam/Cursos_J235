import random
from linear_search import search as l_search
import time

global iteration
iteration = 0

def binary_search(array, left, right, goal):
    """
    binary_search() is meant to execute a binary search
    """
    print(f'Finding {goal} between {left} and {right}')
    global iteration
    iteration = iteration + 1
    print('__________________________________________')

    middle = left + (right - 1) // 2
    print(middle)

    if left > right or left == right or middle > right:
        return -1

    if array[middle] == goal:
        return middle
    elif array[middle] < goal:
        return binary_search(array, middle + 1, right, goal)
    elif array[middle] > goal:
        return binary_search(array, left, middle - 1, goal)


def main():
    goal = int(input('Indicate wich number you do want to find: '))
    size = int(input('Type list size: '))
    print(iteration)

    #sorted() is a method for sorting elements within an iterable
    numbers = sorted([random.randint(1,1000) for i in range(size)])

    print('\n\nThe array is: ', end = '')
    print(numbers, '\n\n')

    print('Starting binary search...')
    start_b = time.time()
    print('..........................................\n\n')
    response = binary_search(numbers, 0, len(numbers), goal)
    print('\n\n..........................................')
    print(f'{goal} {"has been found" if (response != -1) else "could not been found"} in list')
    end_b = time.time()
    runtime_b = end_b - start_b
    print('..........................................\n\n')

    print('Starting linear search...')
    start_l = time.time()
    print('..........................................')
    response_2 = l_search(numbers, goal)
    print(f'{goal} {"has been found" if response_2[0] else "could not been found"} in list')
    end_l = time.time()
    runtime_l = end_l - start_l
    print('..........................................')


    message = f"""
++++++++++++++++++++++++++++++++++++++++++++++++
| Binary search iterations: {iteration}
| Binary search runtime: {runtime_b}
| Linear search iterations: {response_2[1]}
| Linear search runtime: {runtime_l}
++++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(message)



if __name__ == '__main__':
    main()
