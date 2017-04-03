'''
 '    COIS 4470H | Modeling and Simulation
 '      Assignment 4, Question 1
 '
 '    Author: Matthew Barnes
 '    Title:  Variable Generator
 '
 '    Description:
 '      Generates a number between -3 and 4, and then uses the 
 '      following cdf (cumulative distribution function) to 
 '      map the results:
 '
 '          / 0,                       x<= -3
 '   F(x) = | (1/2) + (x/6),        -3 < x <= 0
 '          | (1/2) + ((x^2)/32),    0 < x <= 4  
 '          \ 1,                        x > 4
 '
 '      Following that, it puts the results into a histogram.
'''

import random
import matplotlib.pyplot as plt

num_rand = 1000

rand = []
results = []
offset_counter = 0

# calulate the results from the CDF provided above.
for i in range(num_rand):
  rand.append(((random.random()) * 7) - 3)
  # print(str(i) + ":  " + str(rand))

  if (rand[i] <= -3):
    results.append(0)

  elif (rand[i] <= 0):
    results.append(0.5 + (rand[i] / 6))

  elif (rand[i] <= 4):
    results.append(0.5 + ((rand[i]*rand[i]) / 32))

  else:
    results.append("error")

# neatly print out results in the terminal with the following code:
'''
for i in range(int(len(results) / 10)):
  offset = i*10

  print("element: \t", end=" ")
  for k in range(0,10):
    print(str(k + offset) + "\t|", end=" ")
  print()

  print("rand:  \t\t", end=" ")
  for j in range(0,10):
    print("%.2f" % rand[j + offset] + "\t|", end=" ")
  print()

  print("result:  \t", end=" ")
  for l in range(0,10):
    print("%.2f" % results[l + offset] + "\t|", end=" ")
  print("\n")
'''

# used to create the plots
plt.subplot(121) # row, col, section (first place)
plt.hist(results, bins=250) # num of bins is the granularity.
plt.ylabel("Frequency")
plt.xlabel("F(x)")

plt.subplot(122) # row, col, section (second place)
plt.hist(rand, bins=250)
plt.ylabel("Frequency")
plt.xlabel("Randomly generated num")

plt.tight_layout() # fixes some overlapping issues with graphs
plt.show()
