from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

"""
 django.http模块中定义了HttpResponse 对象的API
 作用：不需要调用模板直接返回数据
 HttpResponse属性：
    content: 返回内容,字符串类型
    charset: 响应的编码字符集
    status_code: HTTP响应的状态码
"""

"""
hello 为一个视图函数，每个视图函数必须第一个参数为request。哪怕用不到request。
request是django.http.HttpRequest的一个实例
"""


def index(request):
    # 添加两个变量，并给它们赋值
    sitename = 'Django中文网'
    url = 'www.django.cn'
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    mydict = {
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }
    all_article = Article.objects.all()

    # 把两个变量封装到上下文里
    context = {
        'sitename': sitename,
        'url': url,
        'list': list,
        'mydict': mydict,
        'all_article': all_article,
    }
    # 把上下文传递到模板里
    return render(request, 'index.html', context)


def msg(request, name, age):
    return HttpResponse('My name is ' + name + ',i am ' + age + ' years old')