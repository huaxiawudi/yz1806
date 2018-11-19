# l1 = ['a','b','c']
# l2 = [1,2,3]
# res = zip(l1,l2)
# d1 = dict(res)
# for value in res:
#     print(value)
# # print(res)
# print(d1)

import re
s1 = "hell11tom11hello"
res = re.search(r'(\d)([a-zA-Z]+)(\d)',s1,re.I)
print(res)
print(res.groups())
print(res.group(2))