from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Post


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def all_posts(request):
    posts = Post.objects.all().order_by("-timestamp")
    return render(request, "network/all_posts.html", {
        "posts": posts
    })

@login_required
def profile(request, username=None):
    if username is None:
        username = request.user.username

    try:
        # Get the user
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, "network/profile.html", {
            "message": "User not found."
        })
    
    # Get the user's posts
    posts = Post.objects.filter(user=user).order_by("-timestamp")
    
    return render(request, "network/profile.html", {
        "user": user,
        "posts": posts
    })

@login_required
def following(request):
    user = request.user
    following = user.following.all()
    posts = Post.objects.filter(user__in=following).order_by("-timestamp")
    return render(request, "network/following.html", {
        "posts": posts
    })

@login_required
def follow(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, "network/profile.html", {
            "message": "User not found."
        })
    
    request.user.following.add(user)
    return HttpResponseRedirect(reverse("profile", args=[username]))

@login_required
def unfollow(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, "network/profile.html", {
            "message": "User not found."
        })
    
    request.user.following.remove(user)
    return HttpResponseRedirect(reverse("profile", args=[username]))

@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST["content"]
        post = Post(user=request.user, content=content)
        post.save()
        return HttpResponseRedirect(reverse("all_posts"))
    else:
        return render(request, "network/create_post.html")

@login_required
def edit_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, "network/all_posts.html", {
            "message": "Post not found."
        })
    
    if request.method == "POST":
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect(reverse("all_posts"))
    else:
        return render(request, "network/edit_post.html", {
            "post": post
        })

@login_required
def like(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, "network/all_posts.html", {
            "message": "Post not found."
        })
    
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("all_posts"))

@login_required
def unlike(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, "network/all_posts.html", {
            "message": "Post not found."
        })
    
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse("all_posts"))

@login_required
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, "network/all_posts.html", {
            "message": "Post not found."
        })
    
    post.delete()
    return HttpResponseRedirect(reverse("all_posts"))
