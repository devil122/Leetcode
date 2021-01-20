#方法一：暴力求解，转换成字符串翻转
def reverse1(x):
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
def reverse2(x):
    y,res = abs(x),0
    boundry = (1<<31)-1 if x>0 else (1<<31)  #1<<31 ==2**31
    while y !=0:
        res = res*10+y%10
        if res>boundry:
            return 0
        y //=10
    return res if x>0 else -res
#测试
x = int(input("x: "))
print(reverse2((x)))
