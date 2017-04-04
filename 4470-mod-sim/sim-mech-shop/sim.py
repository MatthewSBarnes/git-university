# python3.6

'''
'
' Mechanic's shop Simulation.
'
' Imports:
'   simpy: Simulations in Python
'   numpy: generation of random numbers with more distributions
'   random: generation of random numbers
'   matplotlib.pyplot: used to create the graphs dynamically
'   time: for timestamp purposed
'   datetime: to convert timestamp to human readable format
'
' User-Defined:
'   customer: user defined class for customer generator
'
'''

import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import math
from functools import partial, wraps

from customer import customer

NUM_CUSTOMERS = 10
NUM_DAYS = 1
IAT = 10
DAY_LENGTH = 420
ARR_per_day = []
BYE_per_day = []
days = []


# generates customers randomly
def source(env, NUM_CUSTOMERS, interval, mech, DAY_LENGTH, ARR_per_day, BYE_per_day):
    count_ARR = 0
    count_BYE = 0
    
    for i in range(NUM_CUSTOMERS):
        count_ARR += 1
        
        #create a joblength with a uniform distribution of being job_length +/- 5
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

'''
'
' MONKEY PATCH MECH RESOURCE METHODS
'
'''

def patch_resource(resource, pre=None, post=None):
    """Patch *resource* so that it calls the callable *pre* before each
    put/get/request/release operation and the callable *post* after each
    operation.  The only argument to these functions is the resource
    instance.
    """
    def get_wrapper(func):
        # Generate a wrapper for put/get/request/release
        @wraps(func)
        def wrapper(*args, **kwargs):
            # This is the actual wrapper
            # Call "pre" callback
            if pre:
                pre(resource)

            ''' NO PRE SO PRE WONT BE CALLED '''
                
            ''' DO THE MECH OP '''
            
            # Perform actual operation
            ret = func(*args, **kwargs)
            
            ''' POST CALLBACK '''

            # Call "post" callback
            if post:
                post(resource)
            
            return ret
        return wrapper
                
        # Replace the original operations with our wrapper
    for name in ['put', 'get', 'request', 'release']:
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))



def monitor(data, resource):
    """This is our monitoring callback."""
    item = (
        math.floor(resource._env.now),  # The current simulation time
        resource.count,  # The number of users 
        len(resource.queue),  # The number of queued processes
    )
    data.append(item)

env = simpy.Environment()
mech = simpy.Resource(env, capacity=3)

'''
' BEGIN MONKEY PATCH
' Monkey patch the mech resource for monitoring state changes
'''

data = []
# Bind *data* as first argument to monitor()

monitor = partial(monitor, data)
patch_resource(mech, post=monitor)  # Patches (only) this resource instance


'''
' END MONKEY PATCH
''' 
env.process(source(env, NUM_CUSTOMERS, IAT, mech, DAY_LENGTH, ARR_per_day, BYE_per_day))
env.run(until=DAY_LENGTH*NUM_DAYS)


'''
' 
' Plot and statistic stuff
'
'''

# days[] must be a list of the same length as NUM_DAYS for the graphs at the bottom.
for i in range(len(ARR_per_day)):
    days.append(i)

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
plt.savefig('./results/%s_graphs.png' % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
plt.show()

print(data)

