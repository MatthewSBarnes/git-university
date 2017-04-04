# python3.6

import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
from customer import customer

NUM_CUSTOMERS = 100000000000000
NUM_DAYS = 100
IAT = 10
DAY_LENGTH = 420
day = 0
ARR_per_day = []
BYE_per_day = []
days = []


for i in range(NUM_DAYS):
    days.append(i)

def source(env, NUM_CUSTOMERS, interval, mech, DAY_LENGTH, ARR_per_day, BYE_per_day, day):
    count_ARR = 0
    count_BYE = 0
    """Source generates customers randomly"""
    for i in range(NUM_CUSTOMERS):
        count_ARR += 1

        job_duration = joblength()
        job_duration = np.random.uniform(job_duration - 5, job_duration + 5,)

        time_of_day = env.now % DAY_LENGTH

        if (time_of_day + job_duration > DAY_LENGTH):
            count_BYE += 1
            c = customer(env, 'Customer %05d' % i, mech, DAY_LENGTH, job_duration, status=1)

        else:
            c = customer(env, 'Customer %05d' % i, mech, DAY_LENGTH, job_duration, status=0)

        env.process(c)

        # wait until next cust arrives
        t = random.expovariate(1.0 / interval)

        # track the number of customers that head to the shop per day
        if ((env.now % DAY_LENGTH) + t > DAY_LENGTH):
            ARR_per_day.append(count_ARR)
            BYE_per_day.append(count_BYE)
            # reset daily variables, and increment day counter
            day += 1
            count_ARR = 0
            count_BYE = 0
        
        yield env.timeout(t)


def joblength():
    n = random.randint(0,3)
    if (n == 0):
        return 15
    elif (n == 1):
        return 20
    elif (n == 2):
        return 25
    else:
        return 30

env = simpy.Environment()
mech = simpy.Resource(env, capacity=3)

env.process(source(env, NUM_CUSTOMERS, IAT, mech, DAY_LENGTH, ARR_per_day, BYE_per_day, day))
env.run(until=DAY_LENGTH*NUM_DAYS)


'''
' 
' Plot and statistic stuff
'
'''

print('\n\nARR_PER_DAY')
print(ARR_per_day)

print('\n\nBYE_PER_DAY')
print(BYE_per_day)

plt.subplot(121)
plt.plot(days, ARR_per_day)
plt.ylabel('Arrivals')
plt.xlabel('Day')

plt.subplot(122)
plt.plot(days, BYE_per_day)
plt.ylabel('Customers Turned Away')
plt.xlabel('Day')

plt.tight_layout()
plt.show()

