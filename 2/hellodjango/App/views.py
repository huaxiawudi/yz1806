from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("<h1>hello Django</h1>")

def hello(req):
    html = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>hello</title>
    </head>
    <body>
    大家好！
    </body>
    </html>
    """
    return HttpResponse(html)