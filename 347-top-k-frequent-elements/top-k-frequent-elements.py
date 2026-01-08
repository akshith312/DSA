class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        res = []
        for i, n in count.items():
            res.append([n,i])
        res.sort()
        
        ans = []
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans
       
        
        