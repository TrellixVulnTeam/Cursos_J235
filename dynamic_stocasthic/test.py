if __name__ == '__main__':
    arr = [2, 3, 4, 5,6, 7, 8, 8, 9, 8, 9, 3, 5, 4, 9, 4]

    ladder = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] + 1 == arr[i + 1]:
            ladder += 1
            i += 1
        else:
            break

    if ladder == len(arr) - 1:
        print('The array is a ladder')
    else:
        print('Array is not')
