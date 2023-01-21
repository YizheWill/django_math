from django import template
register = template.Library()

@register.inclusion_tag('zscore_form.html')
def show_forms():
    z_calc = [ 
        { 'label': 'mean', 'name': 'mean', 'value': 0 },
        { 'label': 'std', 'name': 'std', 'value': 0 },
        { 'label': 'val', 'name': 'val', 'value': 0 },
    ]
    return {'fields': z_calc}