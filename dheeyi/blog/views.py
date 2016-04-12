from django.shortcuts import render
from django.utils import timezone
from myApp.models import Post


def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'dheeyi/post_list.html', {'posts': posts})
