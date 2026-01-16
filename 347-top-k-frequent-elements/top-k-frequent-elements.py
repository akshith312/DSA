class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for i, n in count.items():
            res.append([n,i])
        res = sorted(res)
        ans = []

        while len(ans) < k:
            ans.append(res.pop()[1])
            
        return ans