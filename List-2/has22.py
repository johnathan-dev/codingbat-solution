def has22(nums):
  contains_two = False
  for i in range(len(nums)):
    if(i < len(nums)-1):
      if((nums[i] == 2 and nums[i+1] == 2)):
        contains_two = True
        break
  return contains_two