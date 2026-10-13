# core/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, About, Skill, Project, ProjectImage, 
    Testimonial, Service , ContactMessage
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_description', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'instagram', 'youtube')
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active')
    list_filter = ('is_active',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    ordering = ('order', 'name')

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'is_active', 'display_image')
    list_filter = ('category', 'featured', 'is_active')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'order', 'rating', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('rating', 'is_active')
    ordering = ('order',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Management', {
            'fields': ('status', 'created_at')
        }),
    )

    actions = ['mark_as_read', 'mark_as_unread', 'mark_as_replied']

    @admin.action(description='Mark selected messages as read')
    def mark_as_read(self, request, queryset):
        queryset.update(status='read')

    @admin.action(description='Mark selected messages as unread')
    def mark_as_unread(self, request, queryset):
        queryset.update(status='unread')

    @admin.action(description='Mark selected messages as replied')
    def mark_as_replied(self, request, queryset):
        queryset.update(status='replied')