from django.contrib import admin
from django.urls import path,include
from appointment import views
urlpatterns = [
    path("",views.appointpage,name="appointpages"),
    path("doctors/<str:name>",views.doctor_detail,name='doctor_detail')
]
