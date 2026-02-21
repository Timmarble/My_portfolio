from django import forms
from .models import Project

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'project_url',
                 'image', 'pdf_file', 'additional_files']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'technologies': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, HTML, CSS'}),
        }