public int maxTriple(int[] nums) {
  int max = Math.max(nums[0], nums[nums.length-1]);
  max = Math.max(max, nums[nums.length/2]);
  return max;
}
