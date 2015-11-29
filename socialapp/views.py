from django.shortcuts import render, redirect

from socialapp.models import UserPost
from socialapp.forms import UserPostForm
from socialapp.models import UserPostComment
from socialapp.forms import UserPostCommentForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.order_by('-date_added')
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text)
            user_post.save()
        return redirect('index')


def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserPostCommentForm()
        user_post_comments = UserPostComment.objects.filter(post=post).order_by('-date_added')
        context = {
            'post': post, 
            'form': form, 
            'comments': user_post_comments,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            user_post_comment = UserPostComment(text=text, author=author, post=post)
            user_post_comment.save()
        return redirect(request.path)
