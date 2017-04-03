import simpy

'''
'  Time functions for the simulation
'    Each day has 420 minutes, (7 operating hours * 60 minutes)
'    Seasons last for 3 months each, or 60 operating days, 
'    the mechanic shop is open 5 days a week * 12 weeks = 60 days
'    (to simplify things)
'    
'    **interarrivaltime(env, season)**
'      Determines the IAT of a customer depending on variables 
'        such as the season.
'      
'        TODO: variable on weather
'
'
'
'    **season(env)**
'      Determines the season of the simulation depending on
'        number of minutes passed. Each season is 60 days,
'        or 25200 minutes (using 420 minutes as operating time)
'
'
'''


def interarrivaltime(env, season):
  # random within a reasonable range dependent on the season

'''
take the now (minutes) and then divide that by the number of minutes in a season, 25200; 0.6547 or some thing weird. and then round that number down, and then mod it by 4, and then that will leave you with the correct season, (5th season = 1st season)
'''
def season(env):
  seas = env.now / 60
  if (seas < 1):
  elif
  elif

