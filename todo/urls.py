from django.urls import path
from todo import views

APP_NAME = 'todo'

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:category_slug>/',views.category_detail,name='category_views'),
    path('category/<slug:category_slug>/todo/<int:id>/',views.detail, name='detail'),
    path('tag/<slug:tag_slug>/',views.tag_view, name='tag_view'),
]
