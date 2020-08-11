import random


def generator():
    upper_cases = ['A', 'B', 'C', 'D', 'E']
    lower_cases = ['a', 'c', 'e', 'g', 'h', 'j']
    symbols = ['*', '?', '¿', '¡', '!', '#', '$', '%', '&', '/', '\\']
    numbers = ['1', '2', '3', '4', '5', '6','7','8','9','0']

    chars = upper_cases + lower_cases + symbols + numbers
    password = []

    for i in range(20):
        random_chars = random.choice(chars)
        password.append(random_chars)

    password = "".join(password)
    return password

def main():
    print('Password generator V0.1')
    password = generator()
    print('Your new password is' + password)


if __name__ == '__main__':
    main()
