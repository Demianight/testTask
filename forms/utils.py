from rest_framework.exceptions import ValidationError

from .models import Form
from .validators import fields_validator


def count_fields(form: Form):
    return len(form.field.all())


def guess_form(data: dict):
    fields_validator(data)
    queryset = Form.objects.all()
    queryset = [form for form in queryset if count_fields(form) <= len(data)]

    forms = []
    for form in queryset:
        flag = True
        for field in form.field.all():
            if field.name not in data.keys():
                flag = False
                break
        if flag:
            forms.append(form)

    if len(forms) == 0:
        raise ValidationError('There is no such form')
    return sorted(forms, key=count_fields)[-1].name
