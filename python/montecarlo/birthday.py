import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()

def birthday_coincidence_probability(n, group_size):
    """ Birthday problem for a given group size """
    hits = 0

    for _ in range(n):
        birthdays = np.sort(generator.integers(0, 366, size=group_size))
    
        lastBirthday = -1                   # Check for duplicities in the birthdays array
        for birthday in birthdays:
            if birthday == lastBirthday:
                hits += 1
                break
            lastBirthday = birthday
    
    probability = hits / n
    error = np.sqrt(hits) / n

    return probability, error


def PlotBirthdayProblem(n=10000, group_sizes=range(2, 50)):
    results = np.asarray([birthday_coincidence_probability(n, group_size) for group_size in group_sizes])
        
    probabilities = results[:, 0]
    errors = results[:, 1]

    plt.errorbar(group_sizes, probabilities, yerr = errors)
    plt.title("Narozeninový problém")
    plt.xlabel(r"$n_{g}$")
    plt.ylabel(r"$p$")
    plt.show()

print(birthday_coincidence_probability(10000, 17))
print(birthday_coincidence_probability(10000, 30))