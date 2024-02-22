from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def current_url(context, url_name, *args, **kwargs):
    request = context['request']
    namespace = request.resolver_match.namespace
    return reverse(f"{namespace}:{url_name}", args=args, kwargs=kwargs)
