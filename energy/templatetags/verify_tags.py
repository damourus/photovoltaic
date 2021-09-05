from django import template
import calendar

register = template.Library()


@register.inclusion_tag("energy/tags/form_row.html")
def form_row(form_field):
    return {"form_field": form_field}

@register.filter
def month_abbr(month_number):
    month_number = int(month_number)
    return calendar.month_abbr[month_number]
