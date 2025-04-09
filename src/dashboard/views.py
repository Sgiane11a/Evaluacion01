from django.shortcuts import render, redirect, get_object_or_404
from .models import GuestUser

def guest_user_list(request):
    users = GuestUser.objects.all()
    return render(request, "dashboard/guest_user_list.html", {"users": users})

def guest_user_detail(request, user_id):
    user = get_object_or_404(GuestUser, id=user_id)
    return render(request, "dashboard/guest_user_detail.html", {"user": user})

def guest_user_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        GuestUser.objects.create(name=name, email=email)
        return redirect("guest_user_list")
    return render(request, "dashboard/guest_user_form.html")

def guest_user_update(request, user_id):
    user = get_object_or_404(GuestUser, id=user_id)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.save()
        return redirect("guest_user_detail", user_id=user.id)
    return render(request, "dashboard/guest_user_form.html", {"user": user})

def guest_user_delete(request, user_id):
    user = get_object_or_404(GuestUser, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("guest_user_list")
    return render(request, "dashboard/guest_user_confirm_delete.html", {"user": user})