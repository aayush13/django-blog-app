from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# views - always need to return an HttpResponse or exception

posts = [
    {
        'author': 'Aayush',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'November 27, 2023'
    },
    {
        'author': 'Aayush',
        'title': 'Blog Post 2',
        'content': 'New Post Content',
        'date_posted': 'November 26, 2023'
    }
]


# templating engine is similar to jinja2
def home(request):
    context = {
        'title': 'Homepage',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
