from django import template
"""
    Used for create new tags for templates
"""
# To be a valid tag library
register = template.Library()

@register.filter(name="zip")
def zip_lists(a, b):
    return zip(a, b)