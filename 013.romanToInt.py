'''第13题：
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer

'''
#构建词典，进行遍历
class solution:
    def romanToInt(self,x):
        sum = 0
        dic = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000,
             'IV':3,
             'IX':8,
             'XL':30,
             'XC':80,
             'CD':300,
             'CM':800
        }
        for i,n in enumerate(x):
            sum += dic.get(x[max(i-1,0):i+1],dic[n]) # max(i-1,0)防止开始 i=0时出现[-1:0]的情况
        return sum


#测试
s = solution()
print(s.romanToInt('MCMXCIV'))