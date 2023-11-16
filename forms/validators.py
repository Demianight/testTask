import re

from django.core.validators import RegexValidator
from django.core.validators import validate_email as email_validator
from rest_framework.exceptions import ValidationError

date_validator = RegexValidator(
    regex=r'^\d{2}.\d{2}.\d{4}$|^\d{4}-\d{2}-\d{2}$',
    message='Enter a valid date format: DD.MM.YYYY or YYYY-MM-DD'
)


def phone_validator(value):
    pattern = re.compile(r'^\+\d{1,3} \d{3} \d{3} \d{2} \d{2}$')
    if not pattern.match(value):
        raise ValidationError(
            'Enter a valid phone number format: "+7 xxx xxx xx xx"')


def fields_validator(data: dict):
    validators = {
        'phone': phone_validator,
        'email': email_validator,
        'date': date_validator,
        # 'text':
    }
    for field, value in data.items():
        if field == 'text':  # I didn't need to validate text
            continue
        validator = validators[field]
        try:
            validator(value)
        except Exception:
            raise ValidationError(f'Enter a valid {field}')
