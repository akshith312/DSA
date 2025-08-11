class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        # """
        # Brute force
        # count = {} 
        
        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        
        # arr = []

        # for num, cnt in count.items():
        #     arr.append([num,cnt])
        # arr.sort()


        # res = []

        # while len(res)<k:
        #     res.append(arr.pop()[1])
        # return res

        count ={}

        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1+ count.get(num,0)
        
        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []

        for i in range(len(freq) -1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



        
        