
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("pages.urls")),
    path("appointment/",include("appointment.urls")),
    path("predict/",include("patient.urls")),
    path('logout/', LogoutView.as_view(next_page='/'), name='logoutpage'),
    # path("heartapi",include("api.urls"))
]
