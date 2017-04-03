# python3.6

import simpy
from customer import customer
# from mech_shop_time import interarrivaltime, season


# can also change it to run strictly on time.
NUM_CUSTOMERS = 10000

env = simpy.Environment()
# Create three mechanics
mech = simpy.Resource(env, capacity=3)

for cust_num in range(NUM_CUSTOMERS):
  env.process(customer(env, mech, cust_num, 5, 7))
  # env.process(customer(env, mech, customer, interarrivaltime(env, season(env)), 7))

env.run()
# each day is 420 minutes
# env.run(until=15*420)
