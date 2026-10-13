# core/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import About, Skill, Project, Testimonial, Service, SiteSettings, ContactMessage

from django.views.decorators.csrf import csrf_protect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


def get_settings():
    return SiteSettings.objects.first()

def home(request):
    settings = get_settings()
    about = About.objects.filter(is_active=True).first()
    skills = Skill.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True, featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    services = Service.objects.filter(is_active=True)
    
    context = {
        'settings': settings,
        'about': about,
        'skills': skills,
        'projects': projects,
        'testimonials': testimonials,
        'services': services,
        'section': 'home',
    }
    return render(request, 'core/home.html', context)

def projects(request):
    settings = get_settings()
    all_projects = Project.objects.filter(is_active=True)
    
    # Get unique categories
    categories = set()
    for project in all_projects:
        if project.category:
            categories.add(project.category)
    
    context = {
        'settings': settings,
        'projects': all_projects,
        'categories': sorted(list(categories)),
        'section': 'projects',
    }
    return render(request, 'core/projects.html', context)

def project_detail(request, slug):
    settings = get_settings()
    project = get_object_or_404(Project, slug=slug, is_active=True)
    
    context = {
        'settings': settings,
        'project': project,
        'section': 'project_detail',
    }
    return render(request, 'core/project_detail.html', context)

@require_POST
def toggle_theme(request):
    # Store theme preference in session
    current_theme = request.session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    request.session['theme'] = new_theme
    return JsonResponse({'theme': new_theme})




@require_POST
@csrf_protect
def contact_submit(request):
    try:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Required field validation
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all fields.'
            }, status=400)

        # Length validation
        if (len(name) > 150 or len(email) > 254
                or len(subject) > 250 or len(message) > 10000):
            return JsonResponse({
                'success': False,
                'message': 'One or more fields exceed the allowed length.'
            }, status=400)

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)

        # Basic text sanitization
        name = strip_tags(name)
        subject = strip_tags(subject)
        message = strip_tags(message)

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })

    except Exception:
        # Log the exception server-side in production.
        return JsonResponse({
            'success': False,
            'message': 'Something went wrong. Please try again later.'
        }, status=500)