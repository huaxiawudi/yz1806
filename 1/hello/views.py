def index(environ,start_response):
    html = "<html><head> <meta charset='utf-8'></head><body>大宝剑</body></html>"
    start_response("200 ok",[('Content-Type','text/html')])
    return [html.encode('utf8')]

def login(environ,start_response):
    html = "<html><head> <meta charset='utf-8'></head><body>登录</body></html>"
    start_response("200 ok", [('Content-Type', 'text/html')])
    return [html.encode('utf8')]


def register(environ,start_response):
    html = "<html><head> <meta charset='utf-8'></head><body>注册</body></html>"
    start_response("200 ok", [('Content-Type', 'text/html')])
    return [html.encode('utf8')]