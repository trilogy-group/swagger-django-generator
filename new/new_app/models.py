"""
Do not modify this file. It is generated from the Swagger specification.

"""
from django.urls import reverse
from django.db import models

class data_service(models.Model):
    domain_id = models.IntegerField()
    id = models.IntegerField()
    model_config = models.CharField(max_length=255)
    repo_name = models.CharField(max_length=255)
    class Meta:
        ordering = ('-id',)
        verbose_name = "data_service"
        verbose_name_plural = "data_services"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:data_service_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:data_service_update', args=(self.id,))

class deployment_status(models.Model):
    flow_id = models.IntegerField()
    id = models.IntegerField()
    prod_version_id = models.IntegerField()
    stage_version_id = models.IntegerField()
    class Meta:
        ordering = ('-id',)
        verbose_name = "deployment_status"
        verbose_name_plural = "deployment_statuss"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:deployment_status_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:deployment_status_update', args=(self.id,))

class domain(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('-id',)
        verbose_name = "domain"
        verbose_name_plural = "domains"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:domain_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:domain_update', args=(self.id,))

class flow(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    class Meta:
        ordering = ('-id',)
        verbose_name = "flow"
        verbose_name_plural = "flows"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:flow_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:flow_update', args=(self.id,))

class product(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('-id',)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:product_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:product_update', args=(self.id,))

class task(models.Model):
    domain_id = models.IntegerField()
    env_variables = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    id = models.IntegerField()
    input_schema = models.CharField(max_length=255)
    is_bootstrapped = models.BooleanField()
    is_published = models.BooleanField()
    name = models.CharField(max_length=255)
    output_schema = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    repo_name = models.CharField(max_length=255)
    class Meta:
        ordering = ('-id',)
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:task_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:task_update', args=(self.id,))

