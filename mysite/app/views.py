from django.shortcuts import render 
from app.models import *
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = User.objects.filter(email=email, password=password)
        print("USER:::", user)
        if user.exists():
            return redirect('edit', id=user.first().pk)
        else:
            messages.error(request,'email ou mot de passe incorrect')
            return render(request, 'mysite/login.html')
    else:
        return render(request, 'mysite/login.html')



def edit(request,id):
    print(id)
    user = User.objects.get(pk=id)
    email = user.email
    first_name = user.first_name
    last_name = user.last_name

    if request.method == "POST":

        email = request.POST["email"]
        user.email = email
        user.save()

        return JsonResponse({"email":email})

    else : 
        context = {
            "email" : email,
            "first_name" : first_name,
            "last_name" : last_name,
            "id" : id
        }

    return render(request, 'mysite/edit.html', context)


