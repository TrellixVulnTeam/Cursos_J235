import random

def bubble_sort(arr):

    n = len(arr)

    for i in range(n): #O(n)
        print('\n__________________________________________')
        print(f' i loop sorting {i}')
        print('__________________________________________\n\n')
        for j in range(0, n - i - 1):
            print(f'j loop sorting {j}, ', end = '')
            if arr[j] > arr[j + 1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():

    size = int(input('Type list size: '))
    arr = [random.randint(1,1000) for i in range(size)]
    print(arr,'\n')
    x = bubble_sort(arr)
    print(x)



if __name__ == '__main__':
    main()
