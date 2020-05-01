from django.shortcuts import render, get_object_or_404, redirect
from .controllers import CreateCtrl
from .models import PostModel
from .forms import PostForm
from django.views.generic import View
from django.core.paginator import Paginator
from django.urls import reverse



def posts_show(request):
    posts = PostModel.objects.all()
    paginator = Paginator(posts, 4)
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)
    is_paginated = page.has_other_pages() #если есть другие страницы True else False

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    
    context={
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'main/start.html', context=context)



class PostCreate(CreateCtrl, View):
    form_model = PostForm
    form_temp = 'main/create_post.html'
    raise_exception = True
