import rest_framework_jwt.views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'entries', views.EntryViewSet, base_name='entries')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^sessions/', rest_framework_jwt.views.obtain_jwt_token),
]
