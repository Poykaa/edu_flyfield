from django.db import models
from users.models import UserProfile
from subjects.models import SubjectModel
from django.urls import reverse


class PostModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, db_index=True)
    image = models.ImageField(upload_to='uploads_model', default=None, blank=True, null=True, verbose_name='Зображення')
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    subject = models.ForeignKey(SubjectModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'post_slug': self.slug})