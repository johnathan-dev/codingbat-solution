def centered_average(nums):
  min = nums[0]
  max = nums[0]
  sum = 0
  for i in range(len(nums)):
    if(nums[i] < min):
      min = nums[i]
    if(nums[i] > max):
      max = nums[i]
  for i in range(len(nums)):
    sum += nums[i]
  return (sum - min - max)/(len(nums)-2)