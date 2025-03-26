from django import template

register = template.Library()

@register.filter
def money_filter(value):
    try:
        formatted_value = f"{value:,.2f}".replace(',', ' ').replace('.', ',')
        return formatted_value
    except Exception as e:
        return value