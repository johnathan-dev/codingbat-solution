def double_char(str):
  new_string = ""
  for i in range(len(str)):
    new_string += str[i] + str[i]
  return new_string