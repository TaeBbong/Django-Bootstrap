from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, AdPostForm, ImageForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login

# Create your views here.
def main_page(request):
    return render(request, 'blog/main_page.html', {})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})

def intro_page(request):
    return render(request, 'blog/intro_page.html', {})

def activity_page(request):
    return render(request, 'blog/activity_page.html', {})

def portfolio_page(request):
    return render(request, 'blog/portfolio_page.html', {})

def announce_page(request):
    announcements = Post.objects.order_by('created_date')
    return render(request, 'blog/announce_page.html', {'announcements': announcements})

def announce_detail(request, pk):
    announce = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/announce_detail.html', {'announce': announce})

@login_required
def announce_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('announce_page')
    else:
        form = PostForm()
    return render(request, 'blog/announce_edit.html', {'form': form})

def study_page(request):
    return render(request, 'blog/study_page.html', {})

def seminar_page(request):
    return render(request, 'blog/seminar_page.html', {})

def contact_page(request):
    return render(request, 'blog/contact_page.html', {})

