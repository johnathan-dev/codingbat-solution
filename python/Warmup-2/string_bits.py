def string_bits(str):
  new_string = ""
  for i in range(len(str)):
    if(i%2==0):
      new_string+=str[i]
  return new_string