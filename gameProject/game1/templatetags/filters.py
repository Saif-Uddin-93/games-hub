from django import template

register = template.Library()

@register.filter(name="rm_whitespace")
def rm_whitespace(string:str):
    return string.replace(" ", "")