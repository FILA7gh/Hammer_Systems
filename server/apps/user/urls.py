from rest_framework.urls import path
from .views import (UserLoginAPIView, ConfirmCodeAPIView, UserProfileAPIView,
                    CodeActivateAPIView)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('confirm/', ConfirmCodeAPIView.as_view()),
    path('', UserProfileAPIView.as_view()),
    path('<int:pk>/code-activate/', CodeActivateAPIView.as_view())
]
