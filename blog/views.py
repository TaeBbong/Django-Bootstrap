from django.shortcuts import render, get_object_or_404
from .models import Post, Portfolio, Activity, Seminar, Study
from .forms import PostForm, ActivityForm, PortfolioForm, SeminarForm
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
    activities = Activity.objects.order_by('created_date')
    acts = []
    index = 0
    length = len(list(activities))
    extra = length % 5

    while True:
        if index + 5 > length:
            acts.append(list(activities)[index:index + extra])
            break
        else:
            acts.append(list(activities)[index:index + 5])
        index += 5

    return render(request, 'blog/activity_page.html', {'activities': acts})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'blog/activity_detail.html', {'activity': activity})

@login_required
def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('activity_page')
    else:
        form = ActivityForm()
    return render(request, 'blog/activity_edit.html', {'form': form})

def portfolio_page(request):
    portfolios = Portfolio.objects.order_by('created_date')
    ports = []
    index = 0
    length = len(list(portfolios))
    extra = length % 3

    while True:
        if index + 3 > length:
            ports.append(list(portfolios)[index:index + extra])
            break
        else:
            ports.append(list(portfolios)[index:index + 3])
        index += 3

    return render(request, 'blog/portfolio_page.html', {'portfolios': ports})

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'blog/portfolio_detail.html', {'portfolio': portfolio})

@login_required
def portfolio_new(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('portfolio_page')
    else:
        form = PortfolioForm()
    return render(request, 'blog/portfolio_edit.html', {'form': form})

def announce_page(request):
    announcements = Post.objects.order_by('created_date')
    anns = []
    index = 0
    length = len(list(announcements))
    extra = length % 5

    while True:
        if index + 5 > length:
            anns.append(list(announcements)[index:index+extra])
            break
        else:
            anns.append(list(announcements)[index:index+5])
        index += 5

    return render(request, 'blog/announce_page.html', {'announcements': anns})

def announce_detail(request, pk):
    announce = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/announce_detail.html', {'announce': announce})

@login_required
def announce_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('announce_page')
    else:
        form = PostForm()
    return render(request, 'blog/announce_edit.html', {'form': form})

def study_page(request):

    return render(request, 'blog/study_page.html', {})

def seminar_page(request):
    seminars = Seminar.objects.order_by('created_date')
    sems = []
    index = 0
    length = len(list(seminars))
    extra = length % 5

    while True:
        if index + 5 > length:
            sems.append(list(seminars)[index:index + extra])
            break
        else:
            sems.append(list(seminars)[index:index + 5])
        index += 5
    return render(request, 'blog/seminar_page.html', {'seminars': sems})

def seminar_detail(request, pk):
    seminar = get_object_or_404(Seminar, pk=pk)
    return render(request, 'blog/seminar_detail.html', {'seminar': seminar})

@login_required
def seminar_new(request):
    if request.method == "POST":
        form = SeminarForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('seminar_page')
    else:
        form = SeminarForm()
    return render(request, 'blog/seminar_edit.html', {'form': form})

def contact_page(request):
    return render(request, 'blog/contact_page.html', {})

