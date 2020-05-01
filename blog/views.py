from .controllers import CreateCtrl, ShowCtrl
from .forms import PostForm
from django.views.generic import View



class ShowPosts(ShowCtrl, View):
    raise_exception = True


class PostCreate(CreateCtrl, View):
    """
    pass the form model and template here
    """
    form_model = PostForm
    form_temp = 'main/create_post.html'
    raise_exception = True
