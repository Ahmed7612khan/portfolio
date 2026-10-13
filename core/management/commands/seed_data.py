# core/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import About, Skill, Service, SiteSettings

class Command(BaseCommand):
    help = 'Seed database with initial data'
    
    def handle(self, *args, **options):
        # Create site settings
        SiteSettings.objects.get_or_create(
            site_name='My Portfolio',
            site_description='Full Stack Developer Portfolio',
            defaults={
                'email': 'your@email.com',
                'github': 'https://github.com/yourusername',
                'linkedin': 'https://linkedin.com/in/yourusername',
            }
        )
        
        # Create about
        About.objects.get_or_create(
            name='John Doe',
            defaults={
                'title': 'Full Stack Developer',
                'bio': 'Passionate full stack developer with 5+ years of experience building web applications.',
                'experience_years': 5,
                'projects_completed': 20,
                'happy_clients': 15,
                'is_active': True,
            }
        )
        
        # Create skills
        skills_data = [
            ('Python', 'backend', 90),
            ('Django', 'backend', 85),
            ('JavaScript', 'frontend', 80),
            ('HTML/CSS', 'frontend', 90),
            ('Tailwind CSS', 'frontend', 85),
            ('PostgreSQL', 'database', 75),
            ('MySQL', 'database', 70),
            ('Git', 'tools', 85),
            ('Docker', 'tools', 70),
            ('AWS', 'tools', 65),
        ]
        
        for name, category, percentage in skills_data:
            Skill.objects.get_or_create(
                name=name,
                category=category,
                defaults={'percentage': percentage, 'is_active': True}
            )
        
        # Create services
        services_data = [
            ('Web Development', 'Building responsive and dynamic web applications.', 'fa-code'),
            ('API Development', 'Creating robust and scalable RESTful APIs.', 'fa-server'),
            ('UI/UX Design', 'Designing beautiful and intuitive user interfaces.', 'fa-paint-brush'),
        ]
        
        for title, description, icon in services_data:
            Service.objects.get_or_create(
                title=title,
                defaults={'description': description, 'icon_class': icon, 'is_active': True}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))