from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('create', views.create),
    path('shows/<int:show_id>', views.view_show),
    path('delete/<int:show_id>', views.delete_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('update/<int:show_id>', views.update),
]
