from rest_framework import serializers

from .models import Field, Form


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['name']


class FormSerializer(serializers.ModelSerializer):
    fields = serializers.SerializerMethodField('get__fields')

    class Meta:
        model = Form
        fields = ['id', 'name', 'fields',]

    # Cause ModelSerializer already has get_fields method
    def get__fields(self, obj: Form):
        return [f.name.lower() for f in obj.field.all()]
