# python3.6

import simpy
from example_car import car
from example_driver import driver

env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)

for i in range(4):
  env.process(car(env, 'Car %d' %i, bcs, i*2, 5))

#car = Car(env)

#env.process(driver(env, car))
env.run(until=15)
