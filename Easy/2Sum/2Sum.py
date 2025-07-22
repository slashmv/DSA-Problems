# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
# def main():
#     solution = Solution()
#     nums = [2,7,11,15]
#     target = 9
#     print(solution.twoSum(nums,target))

# OR

class Solution:
    def twoSum(self, nums, target):
        temp = {}
        for i,num in enumerate(nums):
            rem = target - num
            if rem in temp:
                return[temp[rem], i]
            temp[num] = i

solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums,target))

