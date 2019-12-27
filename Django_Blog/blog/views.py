from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 3 
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post':post})
