from __future__ import (absolute_import, division, print_function, unicode_literals)

from rest_framework import viewsets, mixins, permissions

from .models import {% for model in models %}{{ model.name }}{% if not loop.last %}, {% endif %}{% endfor %}

from .serializers import {% for model in models %}{{ model.name }}Serializer{% if not loop.last %}, {% endif %}{% endfor %}


{% for model in models %}
class {{ model.name }}ViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = {{ model.name }}.objects.all()
    serializer_class = {{ model.name }}Serializer
    # permission_classes = [permissions.IsAuthenticated]

{% endfor %}
