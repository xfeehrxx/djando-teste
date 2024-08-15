from django.views.generic import TemplateView, ListView
from .models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class PostView(ListView):
    model = Post
    template_name='post.html'
    context_object_name = 'all_posts_list'