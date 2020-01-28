from .models import {% for model in models %}{{ model.name }}{% if not loop.last %}, {% endif %}{% endfor %}

from rest_framework import serializers

{% for model in models %}
class {{ model.name }}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {{ model.name }}
        fields = ({% for field in model.fields %}'{{ field.name }}', {% endfor %})

{% endfor %}
