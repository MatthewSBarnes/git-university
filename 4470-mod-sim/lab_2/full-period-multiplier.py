#!/usr/bin/python3
#==================================================
# Matthew Barnes
# 0555121
# 
# COIS 4470H Modelling and Simulation
# 
# Lab
#     Finding Full period multipliers
#===================================================


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# prime_list2 = [2, 3, 5, 7]


print("\nprime modulus\ttotal fpm\tsmallest fpm\tall fpms")
for m in prime_list:
  count = 0
  fpm_list = []
  smallest = m  
  for a in range(1, m):
    p = 1
    x = a
    # print ("smallest is " + str(m)) 
    while (x != 1):
      p = p + 1 
      x = (a*x) % m
    if (p == m-1):
      # print(str(a) + " is a full period multiplier of " + str(m))
      fpm_list.append(a)
      count = count + 1
      # print(str(a) + " < " + str(smallest) + " is " + str(a < smallest))
      if (a < smallest):
        smallest = a
        # print ("smallest changes to: " + str(smallest))
  print(str(m) + "\t\t    " + str(count) + "\t\t    " + str(smallest) + "\t\t    " + str(fpm_list))
print("\n")


#  print("\n======================================================================================")
#  print("For prime modulus " + str(m) + " there are " + str(count) + " full period multipliers.") 
#  if (count > 0):
#    print("For prime modulus " + str(m) + " the smallest full period multiplier is " + str(smallest))
#  print("======================================================================================\n")

