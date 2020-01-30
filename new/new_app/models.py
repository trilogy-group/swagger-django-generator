"""
Do not modify this file. It is generated from the Swagger specification.

"""
from django.urls import reverse
from django.db import models

class data_service(models.Model):
    domain = models.ForeignKey("new_app.domain", on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
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
    flow = models.ForeignKey("new_app.flow", on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    prod_version = models.ForeignKey("new_app.flow_version", on_delete=models.CASCADE, related_name='test')
    stage_version = models.ForeignKey("new_app.flow_version", on_delete=models.CASCADE)
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
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey("new_app.product", on_delete=models.CASCADE)
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

class flow_version(models.Model):
    flow = models.ForeignKey("new_app.flow", on_delete=models.CASCADE)
    flow_json = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    version = models.FloatField()
    class Meta:
        ordering = ('-id',)
        verbose_name = "flow_version"
        verbose_name_plural = "flow_versions"

    def __unicode__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('new_app:flow_version_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('new_app:flow_version_update', args=(self.id,))

class product(models.Model):
    id = models.IntegerField(primary_key=True)
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
    domain = models.ForeignKey("new_app.domain", on_delete=models.CASCADE)
    env_variables = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
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

