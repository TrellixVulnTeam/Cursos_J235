import random

def merge_sort(arr):

    #This scope divides the array in two
    if len(arr) > 1:
        middle = len(arr) // 2
        l_array = arr[:middle:]
        r_array = arr[middle::]

        #Recursive call to the division
        merge_sort(l_array)
        merge_sort(r_array)

        #iterators
        i = 0
        j = 0
        k = 0

        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                arr[k] = l_array[i]
                i += 1
            else:
                arr[k] = r_array[j]
                j += 1

            k += 1


        while i < len(l_array):
            arr[k] = l_array [i]
            i += 1
            k += 1

        while j < len(r_array):
            arr[k] = r_array [j]
            j += 1
            k += 1


def main():

    size = int(input('Type list size: '))
    arr = [random.randint(1,1000) for i in range(size)]

    print('Original array: ', arr)
    print('_' * 100)
    print('Calling merge sort algorithm...')
    merge_sort(arr)
    print('After merge sort algorithm: ', arr)


if __name__ == '__main__':
    main()
