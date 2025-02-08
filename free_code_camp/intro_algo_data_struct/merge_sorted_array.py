def merge(nums1: list[int], n: int, nums2: list[int], m:int):
    
    nums1[m:] = nums2
    nums1.sort()
    return nums1


num1 = [1,2,3,0,0,0]
n = 3
m = 3
num2 = [2,5,6]

print(merge(num1, n, num2, m))
