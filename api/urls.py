from django.urls import path


from .views import api_receiver


urlpatterns = [path("", api_receiver, name="api_receiver")]