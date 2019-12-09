from math import *
import numpy as np
import matplotlib.pyplot as plt

# how to run this file: $python -i myFirstScript.py; f(1.0), or other value

# Exercise 1: Defining functions
def f(x):
    result = np.cos(x)*np.exp(x)
    return result

# Exercise  2: Plotting data
def plotF():
    x_vals = np.linspace(-2.0*np.pi,2.0*np.pi,100)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals)
    plt.show()

np.random.seed(0)
# Exercise 3: Generating random numbers
mu = 5.0
sigma = 2.0
rand_nums1 = np.random.normal(mu,sigma,100000)  # normal distribution
mean1 = rand_nums1.mean()
std1 = rand_nums1.std()
print(mean1)
print(std1)
plt.hist(rand_nums1)
# plt.plot(rand_nums1)
plt.show()

rand_nums2 = np.random.uniform(low=0,high=10,size=100000)
mean2 = rand_nums2.mean()
std2 = rand_nums2.std()
print(mean2)
print(std2)
plt.hist(rand_nums2)
# plt.plot(rand_nums2)
plt.show()