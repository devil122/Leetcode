'''第9题：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
链接：https://leetcode-cn.com/problems/palindrome-number/
'''

class solution:
    #方法1：将整数转换为字符串
    def isPalindrome1(self,x):
        if x >=0 :
            x_str = str(x)
            x_palindrome = x_str[::-1]
            x_converse = int(x_palindrome)
            return True if x_converse==x else False
        else:
            return False

    #方法2：还是字符串，简洁实现
    def isPalindrome2(self,x):
        x_str = str(x)
        l = len(x_str)
        h =l//2
        return x_str[:h]==x_str[-1:-h-1:-1]

    #方法3：直接对其求反转之后的数，不使用字符串反转
    def isPalindrome3(self,x):
        if x<0:
            return False
        y,res = x,0
        while y!=0:
            res = res*10+y%10
            y //= 10
        return True if res==x else False



#测试
s = solution()
print(s.isPalindrome3(0))