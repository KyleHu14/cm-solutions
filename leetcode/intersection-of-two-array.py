class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Sorted = sorted(nums1)
        num2Sorted = sorted(nums2)

        n1Pointer = 0
        n2Pointer = 0

        final = []
        while n1Pointer < len(nums1) and n2Pointer < len(nums2):
            if num1Sorted[n1Pointer] == num2Sorted[n2Pointer]:
                final.append(num1Sorted[n1Pointer])
                n1Pointer += 1
                n2Pointer += 1
            elif num1Sorted[n1Pointer] < num2Sorted[n2Pointer]:
                n1Pointer += 1
            else:
                n2Pointer += 1
            

        return final
