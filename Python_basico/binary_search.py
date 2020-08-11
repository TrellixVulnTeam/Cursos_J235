def main():
    in_user = int(input('Please enter a number: '))
    left = 0.0
    right = max(1.0, in_user)
    middle = (left + right)/2
    epsilon = 0.01

    while abs(middle**2 - in_user) >= epsilon:
        print(f'Left -> {left},\nMiddle -> {middle},\nRight -> {right}\n -----
        ----------------')
        if middle**2 < in_user:
            left = middle
        else:
            right = middle
        middle = (right + left)/2
    print(middle)


if __name__ == '__main__':
    main()
