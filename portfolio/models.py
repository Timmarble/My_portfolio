import os

from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='certificates/')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title

    def filename(self):
        return self.file.name.split('/')[-1]

class CV(models.Model):
    title = models.CharField(max_length=200, default='Timothy Mabele CV')
    file = models.FileField(upload_to='cv/')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'CVs'

    def __str__(self):
        return f"{self.title} - {self.uploaded_at()}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, blank=True)
    project_url = models.URLField( max_length=500,
        blank=True,
        null=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='projects/documents/', blank=True, null=True,
                                help_text='Upload project documentation, report, or presentation')
    additional_files = models.FileField(upload_to='projects/additional/', blank=True, null=True,
                                        help_text='Upload any additional files (ZIP, DOCX, etc.)')

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class ProfileInfo(models.Model):
    """For dynamic content that might change frequently."""
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Profile Information"

    def __str__(self):
        return self.key


# Create your models here.
