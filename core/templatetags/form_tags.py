from django import template

register = template.Library()


@register.filter(name='add_label_class')
def add_label_class(field, css_class):
    return field.label_tag(attrs={'class': css_class})


@register.filter(name='add_widget_class')
def add_widget_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})
