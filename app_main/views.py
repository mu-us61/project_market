from django.shortcuts import render, redirect
from app_main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def index_view(request):
    return render(request, template_name="app_main/index.html")


def items_view(request):
    if request.method == "GET":
        itemsList = Item.objects.filter(owner=None)
        return render(
            request,
            template_name="app_main/items.html",
            context={"itemsList": itemsList},
        )
    if request.method == "POST":
        purchased_item = request.POST.get("purchased-item")
        if purchased_item:
            puchased_item_object = Item.objects.get(name=purchased_item)
            puchased_item_object.owner = request.user
            puchased_item_object.save()
            messages.success(
                request,
                f"tebrikler, {puchased_item_object.name} satın aldınız, fiyatı {puchased_item_object.price}",
            )

        return redirect("items_view_name")


def login_view(request):
    if request.method == "GET":
        return render(request, template_name="app_main/login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login succesful")
            return redirect("items_view_name")
        else:
            messages.error(request, "login unsuccessful")
            return redirect("login_view_name")


def register_view(request):
    if request.method == "GET":
        return render(request, template_name="app_main/register.html")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("post")
        if form.is_valid():
            print("valid")
            form.save()  # burada kullanıcıyı database ekliyor
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have registered succesfully")
            return redirect("index_view_name")
        else:
            messages.error(request, f"some error occured {form.error_messages}")
            return redirect("register_view_name")


def logout_view(request):
    logout(request)
    return redirect("index_view_name")
