from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="home"),  
    path('aim_scope', views.aim, name="aim"),
    path('current_issue', views.current, name="current"),
    path('archive', views.archive, name="archive"),
    path('archive/<issue_slug>', views.journal, name="journal"),   
    path('author_guidelines', views.author, name="author"),
    path('issue', views.issue, name="issue"),
    path('manuscript_submit', views.mssubmit, name="mssubmit"),
    path('review_policy', views.reviewpolicy, name="reviewpolicy"),
    path('editorial_board', views.editorial_board, name="editorial_board"),
] 


