def sum67(nums):
  sev = True
  sum = 0
  for n in nums:
    if n == 6:
        sev = False
    if sev:
        sum += n
        continue
    if n == 7:
        sev = True
  return sum