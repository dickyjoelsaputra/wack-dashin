from django.urls import path

from . import views

urlpatterns = [
    # DASHBOARD
    path("", views.index_dashboard, name="dashboard-index"),
]