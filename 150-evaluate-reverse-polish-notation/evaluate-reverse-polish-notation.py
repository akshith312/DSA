class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        
        for token in tokens:
            if token == '+':
                nums.append(nums.pop()+nums.pop())
            elif token == '-':
                a,b = nums.pop(), nums.pop()
                nums.append(b-a)
            elif token == '*':
                nums.append(nums.pop()*nums.pop())           
            elif token == '/':
                a,b = nums.pop(), nums.pop()
                nums.append(int(float(b)/float(a)))
            else:
                nums.append(int(token))
        return nums[0]
        
        