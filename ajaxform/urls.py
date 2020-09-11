from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friend/', views.friend_view, name='friend'),
    path('post/ajax/friend', views.post_friend, name='post_friend'),
    path('get/ajax/validate/nickname', views.check_nickname, name="validate_nickname"),
]
