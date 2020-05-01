from .models import PostModel
from django.shortcuts import render, redirect
from django.core.paginator import Paginator



class ShowCtrl:
    def get(self, request):
        posts = PostModel.objects.all()
        last_post = PostModel.objects.first()
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
            'last_post': last_post,
        }

        return render(request, 'main/start.html', context=context)



class CreateCtrl:
    form_model = None
    form_template = None

    def get(self, request):
        get_form = self.form_model
        return render(request, self.form_temp, context={'form': get_form})

    def post(self, request):
        post_form = self.form_model(request.POST, request.FILES)
        if post_form.is_valid():
            if 'img' in request.FILES:
                post_form.img = request.FILES['img']
                post_form.save(commit=True)
                
                return redirect('posts_show')
        else:
            print(f'ERROR: {post_form.errors}')

        return render(request, self.form_temp, context={'form' : post_form})