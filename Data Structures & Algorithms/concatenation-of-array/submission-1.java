class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] dblNums = new int[nums.length * 2];
        for(int i = 0; i < nums.length; i++){
            dblNums[i] = dblNums[i+nums.length] = nums[i];
        }
        return dblNums;
    }
}