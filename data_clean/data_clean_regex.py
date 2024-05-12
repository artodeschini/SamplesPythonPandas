import re
import pandas as pd


txt = 'Python is my favorite programming language. I love Python'
m1 = re.findall('Python', txt)

print(m1) # ['Python', 'Python']
print(len(m1)) # 2

# find digit all digit
other_txt = 'Python was released in 1991'
m2 = re.findall('\d', other_txt)

print(m2) # ['1', '9', '9', '1']

m3 = re.findall('\d+', other_txt)
print(m3) # ['1991']

t = 'Hello World'
match_object = re.search('World', t)
print(match_object) # <re.Match object; span=(6, 11), match='World'>
print(match_object.span()) # (6, 11)

txt = 'C is my favorite programing language'
other = re.sub(pattern='C', repl='Python', string=txt) # not implece

print(other)


