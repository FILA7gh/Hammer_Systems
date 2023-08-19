from django.contrib import admin
from django.urls import path, include

from .settings.swagger import urlpatterns as swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    # users
    path('api/v1/users/', include('server.apps.user.urls')),

]

urlpatterns += swagger
