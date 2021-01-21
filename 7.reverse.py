''' 第7题：
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
'''
class solution:
    #方法一：暴力求解，转换成字符串翻转
    def reverse1(self,x):
        if -10<x<10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -(2**31) < x < (2**31)-1 else 0

    #方法二：
    def reverse2(self,x):
        y,res = abs(x),0
        boundry = (1<<31)-1 if x>0 else (1<<31)  #1<<31 ==2**31
        while y !=0:
            res = res*10+y%10
            if res>boundry:
                return 0
            y //=10
        return res if x>0 else -res
#测试
s = solution()
print(s.reverse2(-756))
