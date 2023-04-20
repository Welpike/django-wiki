from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path('random', views.random_article, name="random_article"),
    path('view/<str:slug>', views.view_article, name="view_article"),
    path('new', views.create_article, name="create_article"),
    path('edit/<int:article_pk>', views.edit_article, name="edit_article"),
    path('delete/<int:article_pk>', views.delete_article, name="delete_article"),
]
