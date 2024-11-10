

from django.urls import path
from patient.views import SignupView,LoginupView,PredictionPageView,ResultPageView

urlpatterns = [
   
    path("",PredictionPageView.as_view(),name='predictpage'),
    path("result/",ResultPageView.as_view(),name='resultpage'),
    path("signup/",SignupView.as_view(),name='signuppage'),
    path("login/",LoginupView.as_view(),name='loginpage'),
  
]
