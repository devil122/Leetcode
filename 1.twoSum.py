#方法一
def twoSum1(nums,target):
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
def twoSum2(nums,target):
    hashmap = {}
    for idx,num in enumerate(nums):
        hashmap[num] = idx
    for i,num in enumerate(nums):
        j = hashmap.get(target-num)
        if j is not None and j != i:
            return [i,j]


nums = input("list: ")
target = int(input("target: "))
nums_list = nums.split()
nums_list = [int(nums_list[i]) for i in range(len(nums_list))]
print(twoSum2(nums_list,target))
