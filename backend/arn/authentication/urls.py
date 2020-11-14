from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithEmailView, ArnUserCreate, HelloWorldView

urlpatterns = [
    path('token/obtain/', ObtainTokenPairWithEmailView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', ArnUserCreate.as_view(), name="create_user"),
    path('hello/', HelloWorldView.as_view(), name="hello_world")
]
