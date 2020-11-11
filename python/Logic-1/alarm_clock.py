def alarm_clock(day, vacation):
  if(not vacation and (day < 6 and day > 0)):
    return "7:00"
  elif((vacation and (day < 6 and day > 0)) or (not vacation and (day < 1 or day > 5))):
    return "10:00"
  return "off"