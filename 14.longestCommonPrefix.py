'''第14题：
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
链接：https://leetcode-cn.com/problems/longest-common-prefix/
'''
class solution:
    #方法1：Python 特性，取每一个单词的同一位置的字母，看是否相同。
    def longestCommonPrefix1(self, strs):
        res = ""
        a = zip(*strs) #返回一个对象
        print(a)
        for tmp in zip(*strs):   #zip()将对应元素打包成一个个元组，返回列表长度与最短的对象相同，*将元组解压为列表
            print(tmp)
            tmp_set = set(tmp)   #set创建一个无序不重复元素集
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
    #方法2：从第一个词开始找，依次缩小范围，需要遍历所有单词
    def longestCommonPrefix2(self,strs):
        if not strs:
            return ""
        res = strs[0]
        i = 1
        while i<len(strs):
            while strs[i].find(res) !=0:   #找不到就返回 -1，继续缩小长度，找到了返回起始索引值（应该是0）
                res = res[:len(res)-1]
            i += 1
        return  res



s = solution()
print(s.longestCommonPrefix2(["flower","flower","flower","flower"]))
