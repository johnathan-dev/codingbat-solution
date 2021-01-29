public int sum67(int[] nums) {
  boolean noAdd = false;
  int sum = 0;
  for(int i=0; i<nums.length; i++){
    if(nums[i] == 6){
      noAdd = true;
    }
    if(!noAdd){
      sum += nums[i];
    }
    if(nums[i] == 7){
      noAdd = false;
    }
  }
  return sum;
}
