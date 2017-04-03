#!/usr/bin/python3
#==================================================
# Matthew Barnes
# 0555121
# 
# COIS 4470H Modelling and Simulation
# 
# Lab
#     Lehmer Random Number Generator
#
#  Using the following formula, generate 100 random
#    numbers in the interval (0,1), seed x_0 = 17.
# 
#       x_(i+1) = (ax_i) mod m || i = 0, 1, 2, ...
#
#   let m = 31, a = the maximum period [of 31] (24)
#
#===================================================

NUM_LOOPS = 100

x = 17 # seeded x_0 as 17
a = 24 # a is the max period of m
m = 31 # prime modulus

for i in range(NUM_LOOPS): 
  x = (a*x) % m
  print (str(i) + ".  " + str(x/m))
print('Done!')
