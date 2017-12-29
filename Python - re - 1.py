"""
@time 2017年12月29日17:50:17
@author Noah
@content Regular Expression
"""
import re #导入 re 模块

#以下匹配 只检查一次 且 检查元素为第一个字符

# .   匹配任意字符一次（除了 \n ）
ma1 = re.match(r'.', 'abcd')
print(ma1.group()) #输出：a

ma11 = re.match(r'..', 'abcd')
print(ma11.group()) #输出：ab

# [...]   a-z A-Z 0-9 匹配字符集
ma2 = re.match(r'[a-zA-Z]', 'amid')
print(ma2.group()) #输出：a

# \d / \D   匹配数字/非数字
ma3 = re.match(r'\d', '1254')
print(ma3.group()) #输出：1

ma4 = re.match(r'\D', 'abc')
print(ma4.group()) #输出：a

# \s / \S   匹配空白/非空白字符
ma5 = re.match(r'\s', ' ')
print(ma5.group()) #输出：  (空白)

ma6 = re.match(r'\S', 'mm')
print(ma6.group()) #输出：m

# /w \ /W   单词字符[a-zA-Z0-9] \ 非单词字符
ma7 = re.match(r'\w', '967abc')
print(ma7.group()) #输出：9

ma8 = re.match(r'\W', '$%& ')
print(ma8.group()) #输出：$