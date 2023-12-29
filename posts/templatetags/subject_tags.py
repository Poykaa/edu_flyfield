from django import template
from django.db.models import Count

from subjects.models import SubjectModel
from posts.models import PostModel

register = template.Library()


@register.inclusion_tag('list_subjects.html')
def show_subjects(sub_selected=0):
    return {'subs': SubjectModel.objects.all(), 'cat_selected': sub_selected}


@register.inclusion_tag('list_posts.html')
def show_all_posts():
    print(123)
    return {'posts': PostModel.objects.all()}
