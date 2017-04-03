import simpy
'''
class Driver(object):
  def __init__(self, env, car):
    self.env = env
    self.action = env.process(self.run(car))

  def run(self, car):
    yield self.env.timeout(3)
    car.action.interrupt()
'''

def driver(env, car):
  yield env.timeout(3)
  car.action.interrupt()
