def cat_dog(str):
  cc = 0
  dc = 0
  for i in range(len(str)-2):
    if(str[i:i+3] == "cat"):
      cc += 1
    if(str[i:i+3] == "dog"):
      dc += 1
  return cc == dc