from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from surfjournal import views

router = routers.DefaultRouter()
router.register(r"surfjournals", views.SurfJournalView, "surfjournal")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
