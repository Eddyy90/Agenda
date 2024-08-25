from django.urls import path
from .views import SignInView

urlpatterns = [
    path('login/', SignInView.as_view(), name='signin'),
    # outras rotas...
]
