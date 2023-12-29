from django.shortcuts import render, get_object_or_404
from posts.models import PostModel
from .models import SubjectModel


def get_subject(request, subject_slug):
    if request.method != 'GET':
        return render(request, 'base.html')
    subject = get_object_or_404(SubjectModel, slug=subject_slug)
    posts = PostModel.objects.filter(subject=subject)
    data = {
        'title': subject.name,
        'posts': posts
    }
    return render(request, 'index.html', context=data)