from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from .models import BlogPost 
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    #list out objects 
    #could be a search 
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()  
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    print(context)
    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    #create objects with a form 
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()
        form = BlogPostModelForm()
        return redirect(blog_post_list_view)
    template_name = 'blog/create.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    #1 object -> detailed view 
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'post': post}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
        return redirect(blog_post_list_view)
    template_name = 'blog/update.html'
    next_url = "/blog/" + post.slug + "/edit/"
    context = {'post': post, 'form': form, "next_url": next_url}
    return render(request, template_name, context) 

@staff_member_required
def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        post.delete()
        return redirect(blog_post_list_view)
    context = {'post': post}
    return render(request, template_name, context) 