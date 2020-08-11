def insertion(arr):

    """
    Algorithm
    To sort an array of size n in ascending order:

        1: Iterate from arr[1] to arr[n] over the array.

        2: Compare the current element (key) to its predecessor.

        3: If the key element is smaller than its predecessor,
        compare it to the elements before. Move the greater elements
        one position up to make space for the swapped element.
    """

    l = len(arr)

    for i in range(1, l):

        head = arr[i]

        j = i - 1

        while j >= 0 and head < arr[j]:
            arr[j + 1] = arr [j]
            arr[j] = head
            j -= 1

    return arr


def main():
    arr = [1, 45, 14, 52, 34, 23, 65, 98, 105, 68]
    """
    i = 1, head = 45, arr[j] = 1 → Ommit while loop
    i = 2, head = 12, arr[j] = 45 → Enter while loop

        j = 1
        arr[j + 1] = arr[i] = 45
        [1, 45, 45, 52, ...]
        arr[j] = head = 14
        [1, 14, 45, 52, ...]

        j = 0
        head is not minor than arr[j] so ends while

    i = 3, head = 52, arr[j] = 45 → Ommit while loop
    i = 4, head = 34, arr[j] = 52 → Enter while loop

        j = 3
        arr[j + 1] = arr[i] = 52
        [1, 14, 45, 52, 52, 23...]
        arr[j] = head = 34
        [1, 14, 45, 34, 52, 23...]

        j = 2
        arr[j + 1] = arr[3] = 45
        [1, 14, 45, 45, 52, 23...]
        arr[j] = head = 34
        [1, 14, 34, 45, 52, 23...]

        j = 1
        head is not minor than arr[j] so ends while
    """

    print('The given array is: ', arr)
    print('Executing insertion sort...')
    insertion(arr)
    print('After the insertion sort: ', arr)


if __name__ == '__main__':
    main()
