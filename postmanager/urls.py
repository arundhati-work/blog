from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('posts/',views.post_list,name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("posts/new/",views.create_post,name="create_post"),
    path("posts/edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("posts/delete/<int:post_id>/", views.delete_post, name="delete_post")
]