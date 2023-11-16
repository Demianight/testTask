from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=128)
    field = models.ManyToManyField(
        Field, related_name='forms', blank=True
    )

    def __str__(self) -> str:
        return f'{self.name} {[field.name for field in self.field.all()]}'

    def __repr__(self) -> str:
        return f'{self.name} {[field.name for field in self.field.all()]}'
