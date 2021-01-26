'''第20题：
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/va0lid-parentheses
'''
class solution:
    def isValid(self,x):
        dic = {'(':')',
               '{':'}',
               '[':']',
               '?':'?'}
        stack = ['?']
        if (len(x)%2) !=0:
            return False
        for s in x:
            if s in dic:
                stack.append(s)
            elif dic[stack.pop()] != s:
                return False
        return len(stack)==1


#测试
s = solution()
print(s.isValid("){"))