from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Field, Form
from .serializers import FieldSerializer, FormSerializer
from .utils import guess_form


class FormViewSet(GenericViewSet, ListModelMixin):
    serializer_class = FormSerializer
    queryset = Form.objects.all()

    @action(['post'], detail=False)
    def get_form(self, request: Request):
        form_name = guess_form(request.data)
        return Response(form_name)


class FieldViewSet(GenericViewSet, ListModelMixin):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
