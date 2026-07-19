from typing import Optional

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name="get_config")
def get_config(value: str) -> Optional[str]:
    return getattr(settings, value, None)
