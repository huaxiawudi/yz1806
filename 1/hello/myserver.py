from wsgiref.simple_server import make_server
from myApplication import application


# 创建自己的服务器

server = make_server('localhost', 8000, application)
print("服务器启动....8000")
server.serve_forever()