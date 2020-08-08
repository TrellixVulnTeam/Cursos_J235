import random

def search(numbers, goal):

    global iterator
    match = False
    iterator = 0
    #for loop → O(n)
    for element in numbers:
        iterator += 1
        if element == goal:
            match = True
            break

    return [match, iterator]

if __name__ == '__main__':

    goal = int(input('Indicate wich number you do want to find: '))
    size = int(input('Type list size: '))
    numbers = [random.randint(1,1000) for i in range(size)]
    fun = search(numbers, goal)
    #I'm gonna use a ternary operator within the print statement
    print(numbers)
    print(f'The number {goal} {"is" if fun else "is not"} in list')
