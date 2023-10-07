class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        ans=0
        while l<r:
            cur=min(height[l],height[r])*(r-l)
            ans=max(ans,cur)
            if height[l]<height[r]:
                le=height[l]
                while l<r and height[l]<=le:
                    l+=1
            else:
                le=height[r]
                while l<r and height[r]<=le:
                    r-=1
        return ans