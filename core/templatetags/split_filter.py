# core/templatetags/split_filter.py
from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string by the given delimiter
    """
    if isinstance(value, str):
        return value.split(arg)
    return value

@register.filter
def replace(value, arg):
    """
    Replace a string with another string
    Usage: {{ value|replace:"old:new" }}
    """
    if isinstance(value, str):
        args = arg.split(':')
        if len(args) == 2:
            return value.replace(args[0], args[1])
    return value

@register.filter
def get_category_display(value):
    """
    Convert category key to display name
    """
    categories = {
        'backend': 'Backend',
        'frontend': 'Frontend', 
        'database': 'Database',
        'tools': 'Tools & Others',
        'soft': 'Soft Skills'
    }
    return categories.get(value, value.title())