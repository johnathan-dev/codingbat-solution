def count_evens(nums):
  c = 0
  for i in range(len(nums)):
    if(nums[i] % 2 == 0):
      c += 1
  return c