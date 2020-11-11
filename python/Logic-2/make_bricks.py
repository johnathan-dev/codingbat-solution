def make_bricks(small, big, goal):
  return not ((goal % 5 > small) or (goal > (big*5)+small))