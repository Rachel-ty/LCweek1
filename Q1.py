class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s_nums=sorted(nums)
        cur=s_nums[0]
        n=len(nums)
        for i in range(1,n):
            if s_nums[i]==cur:
                return True
            else:
                cur=s_nums[i]
        return False