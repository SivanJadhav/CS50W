from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/", views.greet, name="greet"),
    path("sivan/", views.sivan, name="sivan"),
    path("david/", views.david, name="david"),
    path("brian/", views.brian, name="brian")
]