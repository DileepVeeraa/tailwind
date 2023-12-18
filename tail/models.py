from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class LatestJournal(models.Model):
    sno = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    cover = models.ImageField(upload_to="covers/")

    def __str__(self):
        return self.title

class Archive(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, default="")
    issue_title = models.CharField(max_length=200,default="")
    issue_summary = models.TextField(default="")
    published =models.CharField(max_length=100, default="")
    cover_img =models.FileField(upload_to="archive_covers/",blank=True)
    def __str__(self):
        return self.title  

class IssueArticle(models.Model):
    article_title = models.CharField(max_length=200)
    article_authors =  models.CharField(max_length=200)
    articles_slug = models.CharField(max_length=50, default="")
    pdf = models.FileField(upload_to="issues/")
    pages = models.CharField(max_length=10, default="")
    doi = models.CharField(max_length=200, default="")
    def __str__(self):
        return f"{self.articles_slug} ({self.article_title})"  

class Man_Submit(models.Model):
    author_name =  models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    abstract = models.TextField()
    form_pdf = models.FileField(upload_to="manuscripts/")
    importance = models.TextField()

    def __str__(self):
        return f"{self.title} (by) {self.author_name}"  