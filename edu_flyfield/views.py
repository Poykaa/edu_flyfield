from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def additional(request):
    return render(request, 'additional.html')


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def videos(request):
    return render(request, 'videos.html')
