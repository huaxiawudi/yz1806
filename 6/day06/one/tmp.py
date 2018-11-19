import re

s1 = "ddd12llsll34kskdfk455kkdfk"

# res = re.search(r'[a-zA-Z]*(\d+)[a-zA-Z]*(\d+)[a-zA-Z]*',s1,re.I)
# first和second是组的名字
# ？P<组名>
res = re.search(r'[a-zA-Z]*(?P<first>\d+)[a-zA-Z]*(?P<second>\d+)[a-zA-Z]*',s1,re.I)
print(res.groups())
print(res)
# 通过组名提取匹配的信息
# 能够获取组的方法只有match和search的返回对象
print(res.group('first'),res.group('second'))
