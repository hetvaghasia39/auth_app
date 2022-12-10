from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from app.forms import UserForm, LoginForm, EditForm
from django.contrib.auth import authenticate, login
from app.models import CustomUser
from django.forms.models import model_to_dict


class Signup(View):
    def get(self, request):
        form = UserForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        form = UserForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            user = CustomUser.objects.get(username=username)
            profile_img = request.POST["profile_img"]
            print("profile_img: ", profile_img)
            if profile_img:
                user.compressImage(profile_img)
            user.set_password(password)
            user.save()
            return redirect("login")
        else:
            return render(request, "signup.html", context)


class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        form = LoginForm()
        context = {"form": form, "message": "user does not exit or wrong password"}
        user = authenticate(request, username=username, password=password)
        if user:
            print("user: ", user)
            login(request, user)
            id = request.user.pk
            return redirect(
                f"/profile/{id}/",
            )
        else:
            return render(request, "login.html", context)


class UserProfile(DetailView):
    model = CustomUser
    field = [
        "username",
        "first_name",
        "last_name",
        "email",
        "profile_img",
        "dob",
        "designation",
    ]


class EditProfile(UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "email", "profile_img", "dob", "designation"]


class DeleteProfile(DeleteView):
    model = CustomUser
    success_url = "/signup/"
