public int sum13(int[] nums) {
  int sum = 0;
	for(int i=0; i < nums.length; i++) {
		if(nums[i] != 13 && ((i > 0 && nums[i-1] != 13) || (i == 0 && nums[i] != 13))) {
			sum += nums[i];
		}
	}
	return sum;
}
