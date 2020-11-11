def round_sum(a, b, c):
  return int(round10(a) + round10(b) + round10(c))
def round10(num):
  return round(num, -1)