"""
@time 2017年12月29日17:43:53
@author Noah
@content Regular Expression
"""
import re  # 导入 re 模块

pa1 = re.compile(r'_')  # 匹配字符 '_'
pa2 = re.compile(r'_V', re.I)  # 匹配时忽略大小写（对大小写不敏感）
ma1 = pa1.match('_value')  # 匹配字符串 '_value'
ma11 = pa1.match('value')  # 匹配字符串 '_value'
ma2 = pa2.match('_value')  # 匹配字符串 '_value'

print(ma1.group())  # 输出：_
print(ma1.groups())  # 元组（tuple）形式输出：()
# print(ma11.group())  # 输出：NoneType
print(ma2.group())  # 输出：_v
