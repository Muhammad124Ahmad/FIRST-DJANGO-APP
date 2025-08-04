from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def index(request):
    template = '''<html>
  "This is your first view
  </html>"'''
    return HttpResponse(content=template)

def get_date(request):
    today=date.today()
    template=f'''<html>It is {today}</html>'''
    return HttpResponse(content=template)


