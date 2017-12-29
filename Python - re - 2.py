"""
@time 2017年12月29日20:00:56
@author Noah
@content Regular Expression"""
import re #导入 re 模块

# *   匹配前一个字符0次或无限次
ma1 = re.match(r'.*', 'abcd')
print(ma1.group()) #输出：abcd

# +   匹配前一个字符1次或无限次
ma2 = re.match(r'[\d]+', '1244')
print(ma2.group()) #输出：1244

# ?   匹配前一个字符0次或1次
ma3 = re.match(r'[\w]?', '234bnv')
print(ma3.group()) #输出：2

# {m} / {m, n} 匹配前一个字符m次或者m次到n次
ma4 = re.match(r'[\w]{2,3}', 'a2fvvd')
print(ma4.group())

# *? / +? / ??   匹配模式变为非贪婪模式（尽可能少匹配字符）
ma5 = re.match(r'[\d][\w]+?', '1234jhksdf83hf23hi')
print(ma5.group())