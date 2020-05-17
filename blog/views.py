from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Dipesh',
        'title':'MyFirstBook',
        'content':'First post content',
        'date_posted':'17 May 2020'

    },
    {
        'author':'Paul Coelho',
        'title':'The Alchemist',
        'content':'Second post content',
        'date_posted':'17 May 2005'

    }

]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})



