from rest_framework.serializers import ValidationError


def validate_url(value):
    if not 'youtube.com' in value:
        raise ValidationError('Использована запрещенная ссылка')
