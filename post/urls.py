from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post-create/", views.post_create, name="post_create"),
    path("post-detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("post-update/<int:pk>/", views.post_update, name="post_update"),
    path("post-delete/<int:pk>/", views.post_delete, name="post_delete"),
]