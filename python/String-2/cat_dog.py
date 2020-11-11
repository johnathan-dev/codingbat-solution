def cat_dog(str):
  cc = 0
  dc = 0
  for i in range(len(str)):
    try:
      if(str[i] == "c" and str[i+1] == "a" and str[i+2] == "t"):
        cc += 1
      if(str[i] == "d" and str[i+1] == "o" and str[i+2] == "g"):
        dc += 1
    except:
      continue
  return cc == dc