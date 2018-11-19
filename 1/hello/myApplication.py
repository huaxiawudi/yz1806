import re

from urls import urlpatterns

# 自己的开发框架
def application(environ, start_response):

    # for key in environ:
    #     print(key,'-----',environ[key])


    # 获取path_info
    path_info = environ.get('PATH_INFO','/')
    print(path_info)
    for pattern,func in urlpatterns:
        if re.match(pattern,path_info,re.I):
             return func(environ,start_response)
    # if path_info == '/':
    #    return  index(environ,start_response)

    html = "<html><head> <meta charset='utf-8'></head><body>hello world</body></html>"

    start_response("200 ok",[('Content-Type','text/html')])
    return [html.encode('utf8')]