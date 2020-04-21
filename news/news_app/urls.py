from django.urls import path
from . import views


urlpatterns = [

					path("", views.index, name="index"),
					path("punch/", views.punch, name="punch"),
					path("sun/", views.sun, name="sun"),
					path("vanguard/", views.vanguard, name="vanguard"),
					path("sahara/", views.sahara, name="sahara"),
					path("aljazeera/", views.aljazeera, name="aljazeera"),
					path("sportinglife/", views.sportinglife, name="sportinglife"),

				]