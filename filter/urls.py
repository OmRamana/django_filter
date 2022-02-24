from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filter import views

router = DefaultRouter()
router.register(r'', views.BookViewset)

urlpatterns = [
   path('', include(router.urls)),
]