class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(nums,target):
            index=-1
            low,high=0,len(nums)-1
            
            while high>=low:
                mid=low+(high-low)/2
                
                if nums[mid]==target:
                    index=mid
                if target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            return index
        def last(nums,target):
            index=-1
            low,high=0,len(nums)-1
            
            while high>=low:
                mid=low+(high-low)/2
                
                if nums[mid]==target:
                    index=mid
                if target>=nums[mid]:
                    low=mid+1
                else:
                     high=mid-1
            return index
        
        idx1 = first(nums,target)
        idx2 = last(nums,target)
        
        return(idx1,idx2)
        