def xyz_there(str):
  for i in range(len(str)):
    try:
      if(str[i] == "x" and str[i+1] == "y" and str[i+2] == "z" and (not str[i-1] == ".")):
        return True
    except:
      continue
  return False
