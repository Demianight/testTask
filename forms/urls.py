from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import FieldViewSet, FormViewSet

router = SimpleRouter()
router.register(
    'forms',
    FormViewSet
)
router.register(
    'fields',
    FieldViewSet
)


urlpatterns = [
    path('', include(router.urls))
]
