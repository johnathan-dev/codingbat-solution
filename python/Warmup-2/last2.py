def last2(str):
  end = str[len(str)-2:]
  c = 0
  for i in range(len(str)-2):
    substring = str[i:i+2]
    if(substring == end):
      c += 1
  return c