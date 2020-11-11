def caught_speeding(speed, is_birthday):
  small_ticket = 61
  big_ticket = 81
  if(is_birthday):
    small_ticket += 5
    big_ticket += 5
  if(small_ticket <= speed <= big_ticket):
    return 1
  elif(speed > big_ticket):
    return 2
  return 0