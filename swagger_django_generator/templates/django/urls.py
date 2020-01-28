"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
import {{ module }}.views as views
from rest_framework import routers
from .api import {% for model in models %}{{ model.name }}ViewSet{% if not loop.last %}, {% endif %}{% endfor %}

router = routers.SimpleRouter()
{% for model in models %}router.register(r'{{ model.name|lower }}', {{ model.name }}ViewSet)
{% endfor %}

urlpatterns = [
    {# URLs are traverse in reversed sorted order so that longer ones are evaluated first #}
    {% for relative_url, class_name in entries|dictsort(true)|reverse %}
    url(r"^{{ relative_url }}$", views.{{ class_name }}.as_view()),
    {% endfor %}
]

if settings.DEBUG:
    urlpatterns.extend([
        url(r"^the_specification/$", views.__SWAGGER_SPEC__.as_view()),
        url(r"^ui/(?P<path>.*)$", serve, {"document_root": "ui",
                                          "show_indexes": True})
    ])

urlpatterns += router.urls