from django.shortcuts import render

posts = [
    {
        'author': 'alchermd',
        'title': 'My first ever post',
        'body': 'This blog is the best!',
        'created_at': 'October 19, 2018',
        'published': True,
    },
    {
        'author': 'janeD',
        'title': 'Learning Django',
        'body': 'This framework rocks!',
        'created_at': 'October 19, 2018',
        'published': True,
    },
    {
        'author': 'alchermd',
        'title': 'Why is Python so awesome?',
        'body': 'The language brings tears to my eyes!',
        'created_at': 'October 21, 2018',
        'published': True,
    },
    {
        'author': 'johnD',
        'title': 'Using the Django ORM',
        'body': 'This tutorial will rock your socks off.',
        'created_at': 'October 25, 2018',
        'published': False,
    }
]


def home(request):
    published_posts = [post for post in posts if post.get('published')]
    return render(request, 'blog/home.djt', {'posts': published_posts})


def about(request):
    return render(request, 'blog/about.djt')
