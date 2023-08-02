class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1

        '''
        learnt this afterwards: using set intersection
        return min(set(nums1) & set(nums2) or [-1])

        verbose:
        intersection = set(nums1) & set(nums2)

        if intersection:
            return min(intersection)
        return -1
        '''
