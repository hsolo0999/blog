from .models import PostModel
from django.shortcuts import render, redirect



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