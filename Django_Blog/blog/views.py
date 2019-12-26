from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    object_list = Post.objects.all().order_by("-date")
    paginator = Paginator(object_list, 3)  # 3 Post trong 1 page
    page =  request.GET.get('page')
    try:
        post = paginator.page(page) 
    except PageNotAnInteger:
        # trả về page đầu tiên nếu tham số page không là một số
        post = paginator.page(1)
    except EmptyPage: 
		# trả về page cuối cùng nếu page vượt ngoài số page
        post = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/blog.html',Data,{'post': post})
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post':post})
