import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list()
    if len(kwargs) != 0:
      for k, v in kwargs.items():
        self.contents += v * [k]
    
  def draw(self, num):
    if num < len(self.contents):
      drawn = random.sample(self.contents, num)
      for i in drawn:
        self.contents.remove(i)    
    if num >= len(self.contents):
      drawn = self.contents
      self.contents = list()
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  repetitions = num_experiments
  expected = list()
  for k, v in expected_balls.items():
    expected += v * [k]
  while repetitions > 0:
    if num_balls_drawn < len(hat.contents):
      drawn = random.sample(hat.contents, num_balls_drawn)
    if num_balls_drawn >= len(hat.contents):
      drawn = hat.contents.copy()

    num_expected = len(expected)
    num_match = 0
    for i in expected:
      if i in drawn:
        drawn.remove(i)
        num_match += 1
    
    if num_expected == num_match:
      success += 1
    repetitions -= 1
  approx_probability = success/num_experiments
  return approx_probability
  
