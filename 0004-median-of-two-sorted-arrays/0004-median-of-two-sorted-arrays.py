class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge = nums1 + nums2
        # x = len(merge)
        # merge.sort()
        # print(merge)
        # if x % 2 == 0:
        #     ans = (merge[x//2] + merge[x//2 - 1]) / 2
        # else:
        #     ans = merge[x//2]
        # return(ans)

        m = len(nums1)
        n = len(nums2)
        x1 = 0
        x2 = 0
        i = 0
        j = 0
        for _ in range((n+m)//2 + 1):
            x2 = x1
            if i < m and j < n:
                if nums1[i] > nums2[j]:
                    x1 = nums2[j]
                    j += 1
                else:
                    x1 = nums1[i]
                    i += 1
            elif i >= m:
                x1 = nums2[j]
                j += 1
            else:
                x1 = nums1[i]
                i += 1
            
        if (n+m) % 2 == 1:
            return x1
        else:
            return (x1+x2)/2




