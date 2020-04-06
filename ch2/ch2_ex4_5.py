
from random import shuffle
from math import ceil

def findSmallest(nList):
    l = len(nList)
    smallest = 999999999
    for i in range(l):
        if nList[i] < smallest:
            smallest = nList[i]
    return smallest

def findLargest(nList):
    l = len(nList)
    largest = -999999999
    for i in range(l):
        if nList[i] > largest:
            largest = nList[i]
    return largest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        p = self.choose_p(nums)

        smalls = [num for num in nums if num < p]
        equals = [num for num in nums if num == p]
        larges = [num for num in nums if num > p]

        if k <= len(larges):
            return self.findKthLargest(larges, k)
        elif len(larges) < k <= len(larges) + len(equals):
            return p
        else:
            return self.findKthLargest(smalls, k-len(larges) - len(equals))

    def choose_p(self, nums):
        m = []
        for i in range((len(nums)-1)//5 + 1):
            G = nums[5*i:5*(i+1)]
            if len(G) == 5:
                m.append(sorted(G)[2])
            else:
                m.append(G[-1])

        return self.findKthLargest(m, len(m)//2+1)
        
def findKthLog(nList, k):
    nList.sort()
    return nList[k - 1]
