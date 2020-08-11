import random

def throw_dice(dice_times):
    sequence_of_throws = []

    for _ in range(dice_times):
        throw = random.choice([1, 2, 3, 4, 5, 6])
        throw2 = random.choice([1, 2, 3, 4, 5, 6])
        throw_t = throw + throw2
        sequence_of_throws.append(throw_t)

    return sequence_of_throws


def main(dice_times, attempts):

    #This list will store the values of throws
    throws = []

    for _ in range(attempts):
        sequence_of_throws = throw_dice(dice_times)
        throws.append(sequence_of_throws)

    print('Throws array ->', throws)

    #___________________________________________________________________________
    dice_eq_1 = 0
    for result in throws:
        if 1 in result:
            dice_eq_1 += 1

    probability_1 = dice_eq_1/attempts

    print(f'The probability of getting one (1) is {probability_1}')
    #___________________________________________________________________________
    dice_eq_12 = 0
    for result in throws:
        if 12 in result:
            dice_eq_12 += 1

    probability_12 = dice_eq_12/attempts

    print(f'The probability of getting twelve (12) is {probability_12}')
    #___________________________________________________________________________



if __name__ == '__main__':
    dice_times = int(input('Enter how many times you want to throw a dice: '))
    attempts = int(input('Enter how many attemps should the simulation run: '))

    main(dice_times, attempts)
