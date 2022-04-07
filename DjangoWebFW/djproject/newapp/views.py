from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from datetime import datetime

# Create your views here.
def show(request):
    print("request.method ", request.method)
    print("request.scheme ", request.scheme)
    print("request.body ", request.body)
    print("request.path ", request.path)
    print("request.user ", request.user)
    text = """<h1>In django app page</h1>"""
    return HttpResponse(text)

def movie(request, name):
    print(name)
    text = "<h1>Movie name is: {0}</h1>".format(name)
    return HttpResponse(text)

def movieyear(request, year):
    print(year)
    text = "<h1>Movie name is: {0}</h1>".format(year)
    return HttpResponse(text)

def indexpage(request, username):
    print(username)
    text = "<h1>User name is: {0}</h1>".format(username)
    return HttpResponse(text)

def movieyear(request, year):
    print(year)
    text = "<h1>Movie release year: {0}</h1>".format(year)
    return HttpResponse(text)

def show_emp_details(request, empid, empname):
    text = "<h1>Employee {0} ID is {1}</h1>".format(empid, empname)
    return HttpResponse(text)

def showdate(request, dmdate):
    print("dmdate>>>>>>>>>>>>>>>>>>>>>>", dmdate)
    print("dmdate>>>>>>>>>>>>>>>>>>>>>>", type(dmdate))
    text = "<h1>Date is: {0}</h1>".format(dmdate)
    return HttpResponse(text)


def indextemplatedemo(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def indexvardemo(request):
    template = loader.get_template('indexvardemo.html')
    data = {
        'name': {'nme': 'Rajendra', 'id': 23}
    }
    return HttpResponse(template.render(data))


def indexiftagdemo(request):
    template = loader.get_template('indextagif.html')
    data = {
        'num': 4
    }
    return HttpResponse(template.render(data))


def indefortagdemo(request):
    template = loader.get_template('disp_devices.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana']
    }
    return HttpResponse(template.render(data))






def indeforemptytagdemo(request):
    template = loader.get_template('indexforemptytag.html')
    data = {
        'fruit_list': []
    }
    return HttpResponse(template.render(data))





def indexcycletagdemo(request):
    template = loader.get_template('indexcycletag.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana', 'pineapple', 'watermelon', 'grapes']
    }
    return HttpResponse(template.render(data))






def tempindemo(request):
    template = loader.get_template('tidemo.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana', 'pineapple', 'watermelon', 'grapes']
    }
    return HttpResponse(template.render(data))
