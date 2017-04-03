import simpy


def customer(env, mech, cust_num, interarrival_time, job_duration):
  # Simulate varied interarrival time
  yield env.timeout(interarrival_time)

  # Request one of the servers
  print('Customer %d arriving at %d' % (cust_num, env.now))
  with mech.request() as req:
    yield req

    # Perform the job
    print('Customer %d being served at %d' % (cust_num, env.now))
    yield env.timeout(job_duration)
    print('Customer %d finished being served at %d' % (cust_num, env.now))





'''
class Car(object):
  def __init__(self, env):
    self.env = env
    # Start the run process everytime an instance is created.
    self.action = env.process(self.run())

  def run(self):
    while True:
      print('Start parking and charging at %d' % self.env.now)
      charge_duration = 5

      # We yield the process that process() returns
      # to wait for it to finish

      #We may get interrupted while charging the battery
      try:
        yield self.env.process(self.charge(charge_duration))
      except simpy.Interrupt:
        # When we received an interrupt, we stop chargin and
        # switch to the "driving" state
        print('Was interrupted. Hope the battery is full enough!')

      # The charge process has finished and
      # we can start driving again
      print('Start driving at %d' % self.env.now)
      trip_duration = 2
      yield self.env.timeout(trip_duration)

  def charge(self, duration):
    yield self.env.timeout(duration)
'''


'''
def Car(env):
  while True:
    print('Start parking at %d' % env.now)
    parking_duration = 5
    yield env.timeout(parking_duration)

    print('Start driving at %d' % env.now)
    trip_duration = 2
    yield env.timeout(trip_duration)
'''
