from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import GuestUser
import requests

# Create your views here.


def welcome(request):
    peruvian_food_api = "https://peruvian-food-api.onrender.com"

    response = requests.get(f"{peruvian_food_api}/api/foods")

    if response.status_code == 200:
        data = response.json()
    else:
        data = []

    context = {
        "data": data,
    }
    return render(request, "home/welcome.html", context)


def invitation(request):
    users = GuestUser.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        guest = GuestUser.objects.create(name=name, email=email)
        guest.save()
        return render(
            request,
            "home/guest_user_list.html",
            {"users": users}
        )

def guest_user_list(request):
    users = GuestUser.objects.all()
    return render(request, "home/guest_user_list.html", {"users": users})
