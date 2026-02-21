from django.shortcuts import render, redirect,  get_object_or_404
from .models import Certificate, CV, ProfileInfo, Project
from django.contrib import messages
from .forms import ProjectUploadForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse


def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    profile_info = {item.key: item.value for item in ProfileInfo.objects.all()}
    return render(request, 'portfolio/about.html', {'profile_info': profile_info})

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects_list})


@staff_member_required
def upload_project(request):
    """Handle project uploads"""
    if request.method == 'POST':
        try:
            project = Project(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                technologies=request.POST.get('technologies', ''),
                project_url=request.POST.get('project_url', ''),
                is_featured=request.POST.get('is_featured') == 'on'
            )

            # Handle file uploads
            if 'image' in request.FILES:
                project.image = request.FILES['image']
            if 'pdf_file' in request.FILES:
                project.pdf_file = request.FILES['pdf_file']
            if 'additional_files' in request.FILES:
                project.additional_files = request.FILES['additional_files']

            project.save()
            messages.success(request, 'Project uploaded successfully!')

        except Exception as e:
            messages.error(request, f'Error uploading project: {str(e)}')

        return redirect('projects')

    return redirect('projects')


@staff_member_required
def delete_project(request, project_id):
    """Delete a project"""
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        messages.success(request, 'Project deleted successfully!')
    return redirect('projects')

def certification(request):
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/certification.html', {'certificates': certificates})

def cv(request):
    latest_cv = CV.objects.filter(is_active=True).first()
    return render(request, 'portfolio/cv.html', {'latest_cv': latest_cv})

def contact(request):
    return render(request, 'portfolio/contact.html')

def upload_project(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('projects')
    else:
        form = ProjectUploadForm()
    return render(request, 'portfolio/upload_project.html', {'form': form})

# Create your views here.
