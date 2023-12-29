from django.db import models
from django.urls import reverse

class SubjectModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subjects:subject', kwargs={'subject_slug': self.slug})

    class Meta:
        ordering = ['name']

