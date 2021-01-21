''' 第1题：
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''
class solution:
    #方法一
    def twoSum1(self,nums,target):
        j = -1
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if (nums.count(target-nums[i])==1) & ((target-nums[i])==nums[i]):
                    continue
                else:
                    j = nums.index(target-nums[i],i+1)
                    break
        if j>0:
            return [i,j]
        else:
            return []
    #方法二:哈希字典
    def twoSum2(self,nums,target):
        hashmap = {}
        for idx,num in enumerate(nums):
            hashmap[num] = idx
        for i,num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None and j != i:
                return [i,j]
#测试
s = solution()
print(s.twoSum2([5,5,4,6],10))
