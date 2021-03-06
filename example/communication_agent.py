#!/usr/bin/env python
# encoding: utf-8

import sys

# First Start the server: $> bin/start.py

if __name__ == '__main__':
  
  port = 6000
  if len(sys.argv) > 1:
    port = int(sys.argv[1])

  try:
    from hfo import *
  except:
    print 'Failed to import hfo. To install hfo, in the HFO directory'\
      ' run: \"pip install .\"'
    exit()
  # Create the HFO Environment
  hfo_env = hfo.HFOEnvironment()
  # Connect to the agent server on port 6000 with the specified
  # feature set. See feature sets in hfo.py/hfo.hpp.
  hfo_env.connectToAgentServer(port, HFO_Features.HIGH_LEVEL_FEATURE_SET)
  # Play 5 episodes
  for episode in xrange(5):
    status = HFO_Status.IN_GAME
    
    while status == HFO_Status.IN_GAME:
      # Grab the state features from the environment
      features = hfo_env.getState()
      # Get any incoming communication
      msg = hfo_env.hear()
      # Do something with incoming communication
      print 'Heard: ', msg
      # Take an action and get the current game status
      hfo_env.act(HFO_Actions.DASH, 20.0, 0)
      # Do something with outgoing communication
      hfo_env.say('Message')
      status = hfo_env.step() 
  
    print 'Episode', episode, 'ended with',
    # Check what the outcome of the episode was
    if status == HFO_Status.GOAL:
      print 'goal', hfo.playerOnBall().unum
    elif status == HFO_Status.CAPTURED_BY_DEFENSE:
      print 'captured by defense', hfo.playerOnBall().unum 
    elif status == HFO_Status.OUT_OF_BOUNDS:
      print 'out of bounds'
    elif status == HFO_Status.OUT_OF_TIME:
      print 'out of time'
    else:
      print 'Unknown status', status
      exit()
  # Cleanup when finished
  hfo_env.cleanup()
