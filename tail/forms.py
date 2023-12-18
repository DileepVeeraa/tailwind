from django import forms
from django.core.validators import FileExtensionValidator

ext_validtaor = FileExtensionValidator(['docx','doc'])

class ManSubmit(forms.Form):
    author_name =  forms.CharField(label="Author/Submitter Name")
    title = forms.CharField(label="Title")
    email = forms.EmailField(label="Corespondent Email")
    abstract = forms.CharField(label="Abstract",widget=forms.Textarea)
    form_pdf = forms.FileField(label="Please Upload your file here", help_text="Please upload word(.docx or .doc) File", validators=[ext_validtaor])
    importance = forms.CharField(label="Importance of the Manuscript",widget=forms.Textarea(attrs={"rows":5, "cols":100}))