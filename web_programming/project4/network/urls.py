from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    #API Routes
    path("posts/all", views.all_posts, name="all_posts"),
    path("posts/<str:username>", views.profile, name="profile"),
    path("create_post", views.create_post, name="create_post"),
]
