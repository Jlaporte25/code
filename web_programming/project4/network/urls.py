from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    #API Routes
    path("all_posts", views.all_posts, name="all_posts"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("create_post", views.create_post, name="create_post"),
    path("following", views.following, name="following"),
]
