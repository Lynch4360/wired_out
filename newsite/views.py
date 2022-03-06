from django.shortcuts import render

posts = [
    {
        'author': 'John',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'February 17, 2022'
    },
    {
        'author': 'Maire',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'February 18, 2022'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
