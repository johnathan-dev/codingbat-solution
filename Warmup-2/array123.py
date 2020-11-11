def array123(nums):
  for i in range(len(nums)):
    if((i <= len(nums)-3) and nums[i:i+3] == [1, 2, 3]):
      return True
  return False