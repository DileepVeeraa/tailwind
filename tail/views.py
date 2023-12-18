from django.shortcuts import render
from django.http import HttpResponse
from tail.models import Archive, LatestJournal, IssueArticle, Man_Submit
from tail.forms import ManSubmit
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


# Create your views here.

def index(request):
    latestjournals = LatestJournal.objects.order_by('sno')[0]
    return render(request, "tail/home.html",{
        "latestjournals":latestjournals,
    })

def aim(request):
    return render(request, "tail/aim&scope.html")

def archive(request):
    archives = Archive.objects.all()
    return render(request, "tail/archive.html",{
        "archives":archives,
    })

def reviewpolicy(request):
    return render(request, "tail/reviewpolicy.html")
    
def editorial_board(request):
    return render(request, "tail/editorial_board.html")
        
def author(request):
    return render(request, "tail/author.html")

def current(request):
    archive = Archive.objects.last()
    issues = IssueArticle.objects.filter(articles_slug= archive.slug)
    return render(request, "tail/current.html",{
        "archive":archive,
        "issues":issues
    })    

def issue(request):
    return render(request, "tail/issue.html")

def mssubmit(request):
    form = ManSubmit()
    if request.method == "POST":
        form = ManSubmit(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Your Manuscript Was Submitted Succesfully.....!") 
            manuscript = Man_Submit(
                author_name =form.cleaned_data["author_name"],
                title =form.cleaned_data["title"],
                email =form.cleaned_data["email"],
                abstract =form.cleaned_data["abstract"],
                form_pdf =form.cleaned_data["form_pdf"],
                importance =form.cleaned_data["importance"]
            )
            data = {
                "author_name":form.cleaned_data["author_name"],
                "title":form.cleaned_data["title"],
                "email":form.cleaned_data["email"],
                "abstract":form.cleaned_data["abstract"],
                "importance":form.cleaned_data["importance"]                
            }
            form_pdf = request.FILES['form_pdf']
            """form = ManSubmit()
            attachment = Man_Submit.objects.last()    
            content = f'''Email: {data["email"]}
                        Abstract: {data["abstract"]} 
                        Imporatnce: {data["importance"]}'''        
            mail = EmailMessage(f'{data["title" ]} by {data["author_name"]} ',
                       content,
                       '',
                       ['admin@indicuszoologica.com'])
            mail.attach(form_pdf.name, form_pdf.read(), form_pdf.content_type)
            mail.send()"""
            manuscript.save()
                    
        return render(request, "tail/mssubmit.html", {
        "form":form
        })
    else:
        return render(request, "tail/mssubmit.html", {
        "form":form
        })
    

def journal(request, issue_slug):
    if request.method =="GET":
        archive = Archive.objects.get(slug = issue_slug)   
        issues = IssueArticle.objects.filter(articles_slug= issue_slug)
        return render(request, "tail/issue.html",{
            "archive":archive,
            "issues":issues
        }) 
    else:
        archive = Archive.objects.get(slug = issue_slug)   
        issues = IssueArticle.objects.filter(articles_slug= issue_slug)
        return render(request, "tail/issue.html",{
            "archive":archive,
            "issues":issues
        })
    

 
    
