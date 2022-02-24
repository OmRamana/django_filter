from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filter import views

router = DefaultRouter()
router.register(r'books', views.BookViewset)
router.register(r'authors', views.AuthorViewset)

urlpatterns = [
   path('', include(router.urls)),
]