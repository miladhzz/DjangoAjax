from django.urls import path
from . import views


urlpatterns = [
    path('friend31/', views.friend_view, name='friend31'),
    path('django31/post/ajax/friend', views.post_friend, name='post_friend_django31'),
    path('django31/get/ajax/validate/nickname', views.check_nickname, name="validate_nickname_django31"),
]
