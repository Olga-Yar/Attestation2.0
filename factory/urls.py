from django.urls import path
from rest_framework import routers

from factory.apps import FactoryConfig
from factory.views.company import CompanyViewSet

app_name = FactoryConfig.name

urlpatterns = [
    path('company/', CompanyViewSet.as_view({'get': 'list'})),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve'})),
    path('company/<int:pk>/update/', CompanyViewSet.as_view({'put': 'update'})),
    path('company/create/', CompanyViewSet.as_view({'post': 'create'})),
    path('company/<int:pk>/delete/', CompanyViewSet.as_view({'delete': 'destroy'})),

]

router = routers.SimpleRouter()
router.register('factory', CompanyViewSet)

urlpatterns += router.urls
