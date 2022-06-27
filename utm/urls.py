from django.urls import path

from utm.views import HomeView

urlpatterns = [path("", HomeView.as_view(), name="home")]
