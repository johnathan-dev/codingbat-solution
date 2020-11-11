def string_splosion(str):
  new_string = ""
  for i in range(len(str)+1):
    new_string += str[:i]
  return new_string