# Generated by Django 4.2.4 on 2023-12-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(default='', max_length=100)),
                ('issue_title', models.CharField(default='', max_length=200)),
                ('issue_summary', models.TextField(default='')),
                ('published', models.CharField(default='', max_length=100)),
                ('cover_img', models.FileField(blank=True, upload_to='archive_covers/')),
            ],
        ),
        migrations.CreateModel(
            name='IssueArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_authors', models.CharField(max_length=200)),
                ('articles_slug', models.CharField(default='', max_length=50)),
                ('pdf', models.FileField(upload_to='issues/')),
                ('pages', models.CharField(default='', max_length=10)),
                ('doi', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LatestJournal',
            fields=[
                ('sno', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('cover', models.ImageField(upload_to='covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Man_Submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('abstract', models.TextField()),
                ('form_pdf', models.FileField(upload_to='manuscripts/')),
                ('importance', models.TextField()),
            ],
        ),
    ]
