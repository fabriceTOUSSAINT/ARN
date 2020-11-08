from django.urls import path, include
from arn import views
from arn.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

#  Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The Api URLs are now determined automatically by the router
urlpatterns = [
     path('', include(router.urls))
]
