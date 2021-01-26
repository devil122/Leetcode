'''第26题：
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

'''
#双指针
class solution:
    def removeDuplicates(self,nums):
        p,q = 0,1
        while (q<len(nums)) :
            if nums[p] == nums[q]:
                q += 1
            else:
                nums[p+1] = nums[q]
                p += 1
                q += 1
        print(nums[0:p+1])
        return len(nums[0:p+1])
s = solution()
print(s.removeDuplicates([1,2,2,3,3,3]))