import statistics
import random
import math

def mean(X):
    return statistics.mean(X)


def variance(X):
    mu = mean(X)

    aux = 0
    for x in X:
        aux += (x - mu) ** 2
    return aux/len(X)


def standard_deviation(X):
    return math.sqrt(variance(X))


if __name__ == '__main__':
    X = [random.randint(1,11) for i in range(50)]
    mu = mean(X)
    var = variance(X)
    sigma = standard_deviation(X)

    message = f"""
____________________
{X}
____________________
- mean: {mu}
- variance: {var}
- standard deviation: {sigma}
    """
    print(message)
