from django.contrib import admin
from django.urls import path, include
from .views import our_teams

urlpatterns = [
    # path('', include('tannent.urls')),
    # path('admin/', admin.site.urls),
    path('', our_teams, name='our_teams')
]
