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

NUM_CUSTOMERS = 100000
NUM_DAYS = 50
SHOW_GRAPHS = 0
IAT = 10
DAY_LENGTH = 420
ARR_per_day = []
BYE_per_day = []
days = []
W = []
X = []
Y = []
Z = []
w = x = y = z = 1
total_job_time = 0

# generates customers randomly
def source(env, NUM_CUSTOMERS, interval, mech, DAY_LENGTH, ARR_per_day, BYE_per_day, w, x, y, z, total_job_time):
    count_ARR = 0
    count_BYE = 0
    
    for i in range(NUM_CUSTOMERS):
        count_ARR += 1
        
        #create a joblength with a uniform distribution of being job_length +/- 5
        job = gen_job() 
        job_duration, w, x, y, z = joblength(job, w, x, y, z)
        job_duration = np.random.uniform(job_duration - 5, job_duration + 5,)

        time_of_day = env.now % DAY_LENGTH

        if (time_of_day + job_duration > DAY_LENGTH):
            count_BYE += 1
            c = customer(env, 'Customer %05d' % i, mech, DAY_LENGTH, job_duration, status=1)

        else:
            c = customer(env, 'Customer %05d' % i, mech, DAY_LENGTH, job_duration, status=0)
            total_job_time += job_duration

        env.process(c)

        # wait until next cust arrives
        t = random.expovariate(1.0 / interval)

        # track the number of customers that head to the shop per day
        if ((env.now % DAY_LENGTH) + t > DAY_LENGTH):
            ARR_per_day.append(count_ARR)
            BYE_per_day.append(count_BYE)
            W.append(w)
            X.append(x)
            Y.append(y)
            Z.append(z)
            # reset daily variables, and increment day counter
            count_ARR = 0
            count_BYE = 0
            w = x = y = z = 0
        
        yield env.timeout(t)


def gen_job():
    return random.randint(0,3)

def joblength(n, w, x, y, z):
    if (n == 0):
        j = 15
        w += 1
    elif (n == 1):
        j = 20
        x += 1
    elif (n == 2):
        j = 25
        y += 1
    else:
        j = 30
        z += 1
    return j, w, x, y, z
'''
'
' MONKEY PATCH MECH RESOURCE METHODS
'
'''

def patch_resource(resource, pre=None, post=None):
    """
    Patch *resource* so that it calls the callable *pre* before each
    put/get/request/release operation and the callable *post* after each
    operation.  The only argument to these functions is the resource
    instance.
    """
    def get_wrapper(func):
        # Generate a wrapper for put/get/request/release
        @wraps(func)
        def wrapper(*args, **kwargs):

            #print(func)
            #print(name)

            # This is the actual wrapper
            # Call "pre" callback
            if pre:
                pre(resource)

            """ NO PRE SO PRE WONT BE CALLED """
                
            """ DO THE MECH OP """
            
            # Perform actual operation
            ret = func(*args, **kwargs)
            
            """ POST CALLBACK """

            # Call "post" callback
            if post:
                post(resource)
            
            return ret
        return wrapper
                
    # Replace the original operations with our wrapper
    for name in ['put', 'get', 'request', 'release']: 
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))


def premonitor(data, resource):
    """This is our monitoring callback."""
    item = (
        'pre',
        math.floor(resource._env.now),  # The current simulation time
        resource.count,  # The number of users 
        len(resource.queue),  # The number of queued processes
    )
    data.append(item)


def postmonitor(data, resource):
    """This is our monitoring callback."""
    item = (
        'post',
        math.floor(resource._env.now),  # The current simulation time
        resource.count,  # The number of users 
        len(resource.queue),  # The number of queued processes
    )
    data.append(item)

env = simpy.Environment()
mech = simpy.Resource(env, capacity=3)

'''
BEGIN MONKEY PATCH
Monkey patch the mech resource for monitoring state changes
'''

data = []
#Bind *data* as first argument to monitor()

premonitor = partial(premonitor, data)
postmonitor = partial(postmonitor, data)
patch_resource(mech, post=postmonitor)  # Patches (only) this resource instance

'''
END MONKEY PATCH
'''

env.process(source(env, NUM_CUSTOMERS, IAT, mech, DAY_LENGTH, ARR_per_day, BYE_per_day, w, x, y, z, total_job_time))
env.run(until=DAY_LENGTH*NUM_DAYS)
print('\n  Simulation Finished!')

'''
' 
' Plot and statistic stuff
'
'''

# days[] must be a list of the same length as NUM_DAYS for the graphs at the bottom.
for i in range(len(ARR_per_day)):
    days.append(i)

# The data in a list.
#print(days)
#print('\n\nARR_PER_DAY')
#print(ARR_per_day)
#print('\n\nBYE_PER_DAY')
#print(BYE_per_day)

print('\n\n  ===============================\t\t\t\t\t\t=======================')
print('          Some Statistics        \t\t\t\t\t\t        Authors')
print('  ===============================\t\t\t\t\t\t=======================\n\n')
print('  Number of Days within Simulation: %d\t\t\t\t\t Matthew Barnes + Yashar Morabbi Heravi' % (NUM_DAYS))
print('  Minutes per Day: %d\n' % DAY_LENGTH)

print('  Average number of times Job 0 was requested: %d' % (sum(W)/NUM_DAYS))
print('  Average number of times Job 1 was requested: %d' % (sum(X)/NUM_DAYS))
print('  Average number of times Job 2 was requested: %d' % (sum(Y)/NUM_DAYS))
print('  Average number of times Job 3 was requested: %d\n\n' % (sum(Z)/NUM_DAYS))

print('  Graphs are saved to the ./results/ directory\n\n')


# Create the plots
time_stamp = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
# ARR chart
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.subplot(111)
plt.plot(days, ARR_per_day)
plt.ylabel('Arrivals')
plt.xlabel('Day')
plt.title('Arrivals per Day')
fig = plt.gcf()
fig.canvas.set_window_title('Graph - Number of Arrivals per Day')
plt.savefig('./results/%s_figure_ARR.png' % (time_stamp))
if (SHOW_GRAPHS == 1 ):
    plt.show()
plt.close()


# BYE chart
plt.subplot(111)
plt.plot(days, BYE_per_day)
plt.ylabel('Customers Turned Away')
plt.xlabel('Day')
plt.title('Customers Turned Away per Day')
fig = plt.gcf()
fig.canvas.set_window_title('Graph - Number of Customers Turned Away per Day')

# Fix Layout, save, and show graphs
# plt.tight_layout()
plt.savefig('./results/%s_figure_BYE.png' % (time_stamp))
if (SHOW_GRAPHS == 1 ):
    plt.show()
plt.close()

massaged_data = []

for i in range(len(data)):
    if (data[i][2] < 3 and data[i][3] > 0):
        temp3 = int(data[i][3])
        temp2 = int(data[i][2])
        while ((temp2 < 3) and (temp3 > 0)):
            temp3 -= 1
            temp2 += 1
    else:
        temp3 = data[i][3]
        temp2 = data[i][2]
    new_item = [data[i][0], data[i][1], temp2, temp3]
    massaged_data.append(new_item)

in_queue = 0
total_delay = 0
total_delay_per_day = []
current_day = 0

for i in range(len(massaged_data)-1):
    total_delay += ( massaged_data[i+1][1] - massaged_data[i][1] ) * massaged_data[i][3]
    if ((math.floor(massaged_data[i+1][1] / DAY_LENGTH ) > current_day) or (i == len(massaged_data) - 2 )):
        current_day += 1
        total_delay_per_day.append(total_delay)
        total_delay = 0

#plt.subplot(111)
#plt.plot(days, total_delay_per_day)
#plt.ylabel('Total Delay per Day')
#plt.xlabel('Day')
#plt.savefig('./results/%s_figure_DEL.png' % (time_stamp))
#if (SHOW_GRAPHS == 1 ):
#    plt.show()
#plt.close()

avg_delay_per_day = []
for i in range(len(total_delay_per_day)):
    avg_delay_per_day.append( total_delay_per_day[i] / DAY_LENGTH )

plt.subplot(111)
plt.plot(days, avg_delay_per_day)
plt.ylabel('Average Delay')
plt.xlabel('Day')
plt.title('Average Delay per Day')
fig = plt.gcf()
fig.canvas.set_window_title('Graph - Average Delay per Day')
plt.savefig('./results/%s_figure_AVGDEL.png' % (time_stamp))
if (SHOW_GRAPHS == 1 ):
    plt.show()
plt.close()

# Show both BYE and ARR per day
#plt.subplot(111)
#plt.plot(days, ARR_per_day)
#plt.plot(days, BYE_per_day)
#plt.show()

plt.subplot(111)

plt.plot(days, W, label='Windshield Repair j0')
plt.plot(days, X, label='Oil Change j1')
plt.plot(days, Y, label='Tire Change j2')
plt.plot(days, Z, label='Detailing j3')

plt.xlabel('Day')
plt.ylabel('Number of Jobs')
plt.title('Number of Jobs per Day')
fig = plt.gcf()
fig.canvas.set_window_title('Graph - Number of Jobs per Day')

plt.tight_layout()
plt.legend()
plt.savefig('./results/%s_figure_JOBPDAY.png' % (time_stamp))
if (SHOW_GRAPHS == 1 ):
    plt.show()
plt.close()

print('OTIS')
print(total_job_time+sum(total_delay_per_day))
