from django.shortcuts import render


def post_list(request):
    return render(request, 'dheeyi/post_list.html', {})

