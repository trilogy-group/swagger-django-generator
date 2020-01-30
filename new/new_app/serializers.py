from .models import data_service, deployment_status, domain, flow, flow_version, product, task
from rest_framework import serializers

class data_serviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = data_service
        fields = ('domain', 'id', 'model_config', 'repo_name', )

class deployment_statusSerializer(serializers.ModelSerializer):

    class Meta:
        model = deployment_status
        fields = ('flow', 'id', 'prod_version', 'stage_version', )

class domainSerializer(serializers.ModelSerializer):

    class Meta:
        model = domain
        fields = ('id', 'name', )

class flowSerializer(serializers.ModelSerializer):

    class Meta:
        model = flow
        fields = ('id', 'name', 'product', )

class flow_versionSerializer(serializers.ModelSerializer):

    class Meta:
        model = flow_version
        fields = ('flow', 'flow_json', 'id', 'version', )

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ('id', 'name', )

class taskSerializer(serializers.ModelSerializer):

    class Meta:
        model = task
        fields = ('domain', 'env_variables', 'framework', 'id', 'input_schema', 'is_bootstrapped', 'is_published', 'name', 'output_schema', 'path', 'port', 'repo_name', )

