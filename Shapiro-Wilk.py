# Sapiro-Wilk test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro
seed(0)
data = randn(100)
print(data)
statp = shapiro(data)
print(statp)
