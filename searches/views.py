from django.shortcuts import render
from lblog.models import BlogPost
from .models import SearchQuery 

# Create your views here.

def search_view(request):
    query = request.GET.get('search', None)
    user = None 
    if request.user.is_authenticated:
        user = request.user
    context = {"search":query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        print(blog_list)
    context['blog_list'] = blog_list
    return render(request, 'searches/view.html', context)