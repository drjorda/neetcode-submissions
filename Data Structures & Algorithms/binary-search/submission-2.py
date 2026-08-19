class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mx = len(nums)-1
        mn=0
        while(mn <= mx):
            i=int((mx-mn)/2 + mn)
            if(nums[i] == target):
                return i
            elif(nums[i] > target):
                mx=i- 1
            else:
                mn=i+1
                
        return -1