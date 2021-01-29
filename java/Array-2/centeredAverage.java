public int centeredAverage(int[] nums) {
  int min = nums[0];
  int max = nums[0];
  int total = 0;
  for(int i=0; i<nums.length; i++){
    if(nums[i] < min){
      min = nums[i];
    }
    if(nums[i] > max){
      max = nums[i];
    }
  }
  for(int i : nums){
    total += i;
  }
  total -= min+max;
  return total/(nums.length-2);
}
