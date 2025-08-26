class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        answer = []
        for i in nums:
            sum += i
            answer.append(sum)
        return answer        