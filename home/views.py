from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hey this is django server")


def success_page(request):
    return HttpResponse("<h1>Hello this is succes page</h1>")

def Home(request):
    return render(request,"home/index.html")

def Home(request):
    peoples=[{'name':'shakil','age':21},
             {'name':'rahul meena','age':19},
             {'name':'lokesh bhagat','age':22},
             {'name':'aryan kuttarmare','age':17}]
    
    
    text=""" hello i am shakil kathat from ajmer rajasthan
    """
    
    vegetables=['tomato','carrot',"cucumber",'chilli']
    return render(request,"home/index.html",context={'peoples':peoples, 'text':text,'vegetables':vegetables})

def Contact(request):
    
    return render(request,"home/contact.html",context={})

def About(request):
    
    return render(request,"home/about.html",context={})