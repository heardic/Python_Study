import re

# text = "Hello, my phone is 138-1234-5678"
# pattern = "phone"  # 要找的词
#
# result = re.search(pattern, text)
#
# if result:
#     print("找到了！", result.group())
# else:
#     print("没找到")



# text = "Call me at 138-1234-5678 or 139-8765-4321"
# pattern = r'\d{3}-\d{4}-\d{4}'  # r'' 表示原始字符串，很重要！
#
# result = re.findall(pattern, text)  # findall 找所有匹配的
# print(result)
#
#
# email = "user@example.com"
# pattern = r'^\w+@\w+\.\w+$'  # ^开头 \w+@ 至少一个字符+@ \w+\.\w+ 类似 gmail.com
#
# if re.match(pattern, email):  # match 从开头匹配
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")
#
#
# text = "Hello, world! How are you?"
# words = re.findall(r'\w+', text)  # \w+ 表示连续的字母数字下划线
# print(words)
# # 输出: ['Hello', 'world', 'How', 'are', 'you']
#
# text = "我的电话是 138-1234-5678，不是 139-8765-4321"
# # 把所有电话号码替换成 [保密]
# new_text = re.sub(r'\d{3}-\d{4}-\d{4}', '[保密]', text)
# print(new_text)
# # 输出: 我的电话是 [保密]，不是 [保密]
#
# text = "apple, banana; orange  grape"
# # 按逗号、分号、空格分割
# items = re.split(r'[,;\s]+', text)  # [,;\s]+ 表示一个或多个逗号/分号/空格
# print(items)
# # 输出: ['apple', 'banana', 'orange', 'grape']



import re

print("🌟 正则表达式 re 模块练习大全 🌟\n")

# ==================== 1. \d：匹配一个数字 ====================
print("1. \\d：匹配一个数字")
text = 'a1b2c3'
result = re.findall(r'\d', text)
print(f"文本: '{text}' -> 结果: {result}")
print()

# ==================== 2. \w：匹配字母、数字、下划线 ====================
print("2. \\w：匹配字母、数字、下划线")
text = 'a_1!b@2'
result = re.findall(r'\w', text)
print(f"文本: '{text}' -> 结果: {result}")
print()

# ==================== 3. \s：匹配空白字符（空格、制表符、换行） ====================
print("3. \\s：匹配空白字符")
text = 'a b\tc\nd'  # \t 是制表符，\n 是换行
result = re.findall(r'\s', text)
print(f"文本: 'a b\\tc\\nd' -> 结果: {result} (空格、\\t、\\n)")
print()

# ==================== 4. . ：匹配任意一个字符（除了换行） ====================
print("4. . ：匹配任意一个字符（除了换行）")
text = 'abc aXc a c a\nc'
result = re.findall(r'a.c', text)
print(f"文本: '{text}' -> 结果: {result}")
print("注意：a\\nc 中的 \\n 是换行，. 默认不匹配换行，所以没找到")
print()

# ==================== 5. * ：前面的字符出现 0 次或多次 ====================
print("5. * ：前面的字符出现 0 次或多次")
text = 'a ab abb abbb c'
result = re.findall(r'ab*', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：b 可以出现 0 次（a）或多次（ab, abb, abbb）")
print()

# ==================== 6. + ：前面的字符出现 1 次或多次 ====================
print("6. + ：前面的字符出现 1 次或多次")
text = 'a ab abb abbb'
result = re.findall(r'ab+', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：b 至少出现 1 次，所以单独的 'a' 不匹配")
print()

# ==================== 7. ? ：前面的字符出现 0 次或 1 次 ====================
print("7. ? ：前面的字符出现 0 次或 1 次")
text = 'a ab abb'
result = re.findall(r'ab?', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：b 最多出现 1 次，'abb' 中只匹配 'ab'")
print()

# ==================== 8. {n} ：前面的字符重复 n 次 ====================
print("8. {n} ：前面的字符重复 n 次")
text = '12 123 1234'
result = re.findall(r'\d{3}', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：只匹配连续 3 个数字，'12' 不够，'1234' 匹配前 3 个")
print()

# ==================== 9. {m,n} ：前面的字符重复 m 到 n 次 ====================
print("9. {m,n} ：前面的字符重复 m 到 n 次")
text = '1 12 123 1234 12345'
result = re.findall(r'\d{2,4}', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：匹配 2~4 位数字")
print()

# ==================== 10. [] ：字符集合（匹配其中任意一个） ====================
print("10. [] ：字符集合（匹配其中任意一个）")
text = 'hello world'
result = re.findall(r'[aeiou]', text)
print(f"文本: '{text}' -> 结果: {result}")
print("解释：找出所有元音字母 a,e,i,o,u")
print()

# ==================== 11. ^ ：匹配字符串开头 ====================
print("11. ^ ：匹配字符串开头")
text1 = 'Hello world'
text2 = 'Hi Hello'

match1 = re.search(r'^Hello', text1)
match2 = re.search(r'^Hello', text2)

print(f"文本: '{text1}' -> {'匹配' if match1 else '不匹配'}")
if match1: print(f"  找到: {match1.group()}")

print(f"文本: '{text2}' -> {'匹配' if match2 else '不匹配'}")
print()

# ==================== 12. $ ：匹配字符串结尾 ====================
print("12. $ ：匹配字符串结尾")
text1 = 'Hello world'
text2 = 'world hello'

match1 = re.search(r'world$', text1)
match2 = re.search(r'world$', text2)

print(f"文本: '{text1}' -> {'匹配' if match1 else '不匹配'}")
if match1: print(f"  找到: {match1.group()}")

print(f"文本: '{text2}' -> {'匹配' if match2 else '不匹配'}")
print()

print("🎉 练习结束！你可以修改文本或模式，继续尝试！")

