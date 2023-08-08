import random

def roll_two_dice():
  """Simulates rolling two dice and returns the results."""
  first_die = random.randint(1, 6)
  second_die = random.randint(1, 6)
  return first_die, second_die