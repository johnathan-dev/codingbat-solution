def end_other(a, b):
  checker = ""
  if(len(a) >= len(b)):
    i = -len(b)
    while(i < 0):
      checker += a[i].lower()
      i += 1
    return checker == b.lower()
  else:
    i = -len(a)
    while(i < 0):
      checker += b[i]
      i += 1
    return checker.lower() == a.lower()