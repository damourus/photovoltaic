from django import template

register = template.Library()


@register.inclusion_tag("energy/tags/form_row.html")
def form_row(form_field):
    return {"form_field": form_field}