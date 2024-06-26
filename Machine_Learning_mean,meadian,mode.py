import numpy
from scipy import stats

grades = [100,89,89,90,95] #MEAN (AVERAGE VALUE)
x = numpy.mean(grades)
print(x)

y = numpy.median(grades) #MEDIAN (MIDDLE VALUE)
print(y)

z = stats.mode(grades) #MODE(MOST COMMON VALUE)
print(z)
