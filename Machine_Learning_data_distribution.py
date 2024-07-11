import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
'''
import scipy.stats as stats

# Parameters for the normal distribution
mu = 50
sigma = 10

# Calculating the cumulative probabilities
p_40 = stats.norm.cdf(40, mu, sigma)
p_60 = stats.norm.cdf(60, mu, sigma)

# Probability that x is between 40 and 60
p_40_to_60 = p_60 - p_40
p_40_to_60
'''