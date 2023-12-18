from django.contrib import admin
from .models import LatestJournal, Archive, IssueArticle, Man_Submit

# Register your models here.

admin.site.register(LatestJournal)
admin.site.register(Archive)
admin.site.register(IssueArticle)
admin.site.register(Man_Submit)