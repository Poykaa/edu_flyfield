from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PostModel
from .forms import PostForm
from django.views.generic import CreateView
from users.models import UserProfile


def get_post(request, post_slug):
    post = get_object_or_404(PostModel, slug=post_slug)
    data = {
        'title': f'Пост: {post_slug}',
        'post': post,
    }
    return render(request, 'post.html', context=data)


class AddPost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'addpage.html'
    title_page = 'Додавання посту'
    redirect_field_name = 'home'

    def form_valid(self, form):
        w = form.save(commit=False)
        user = get_object_or_404(UserProfile, user=self.request.user)
        w.author = user
        return super().form_valid(form)
