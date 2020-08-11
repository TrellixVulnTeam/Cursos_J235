import random
import math
import statistics as st

#Simulation
def throw_needle(needles):
    in_circle = 0

    for _ in range(needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            in_circle += 1

    return (4 * in_circle) / needles



def estimate(needles, tries):

    #All estimations of Pi
    estimates = []

    for _ in range(tries):
        estimations = throw_needle(needles)
        estimates.append(estimations)

    #Calling statistic functions
    mean_estimations = st.mean(estimates)
    sigma = st.stdev(estimates)

    #Message of output
    print(f'- Estimation of Pi: {mean_estimations} \n- Sigma: {sigma} \n- Needles {needles}')
    return (mean_estimations, sigma)


def estimate_pi(precition, tries):
    needles = 1000
    sigma = precition

    while sigma >= precition/1.96:
        mean_estimations, sigma = estimate(needles, tries)
        needles *= 2

    return mean_estimations

#______________________________________________________________________________
#Main module
if __name__ == '__main__':
    estimate_pi(0.01, 1000)
