"""
Do not modify this file. It is generated from the Swagger specification.

"""
from django.urls import reverse
from django.db import models

{% for model in models %}
class {{ model.name }}(models.Model):
    {% for field in model.fields %}
    {{ field.name }} = models.{{ field.class }}
    {% endfor %}
    class Meta:
        ordering = ('-id',)
        verbose_name = "{{ model.name }}"
        verbose_name_plural = "{{ model.name }}s"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('{{ app_name }}:{{ model.name|lower }}_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('{{ app_name }}:{{ model.name|lower }}_update', args=(self.id,))

{% endfor %}
