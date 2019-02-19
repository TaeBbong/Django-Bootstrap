from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'blog/main_page.html', {})

def login_page(request):
    return render(request, 'blog/login_page.html', {})

def intro_page(request):
    return render(request, 'blog/intro_page.html', {})

def activity_page(request):
    return render(request, 'blog/activity_page.html', {})

def portfolio_page(request):
    return render(request, 'blog/portfolio_page.html', {})

def announce_page(request):
    return render(request, 'blog/announce_page.html', {})

def study_page(request):
    return render(request, 'blog/study_page.html', {})

def seminar_page(request):
    return render(request, 'blog/seminar_page.html', {})

def contact_page(request):
    return render(request, 'blog/contact_page.html', {})

