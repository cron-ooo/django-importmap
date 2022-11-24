import json

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from ..importmap import Importmap

register = template.Library()


@register.simple_tag
def render_importmap():
    importmap = Importmap()
    importmap.importmap['imports'].update({
        key: static(value)
        for key, value in settings.IMPORTMAP_LOCAL_MODULES.items()
    })
    return mark_safe(json.dumps(importmap.importmap, indent=2))
