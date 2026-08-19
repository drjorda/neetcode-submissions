class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = int(len(nums)/2)-1
        mx = len(nums)-1
        mn=0
        while(mn <= mx):
            i=int((mx-mn)/2 + mn)
            if(nums[i] == target):
                return i
            elif(nums[i] > target):
                mx-=1
            else:
                mn+=1
                
        return -1