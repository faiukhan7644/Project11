from django.shortcuts import render

def redirect (request):
    return render(request,"index.html")


def loginCheck (request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username =="faiukhan" and password =="password":
        return render(request,"welcome.html")

    else:
        return render(request,"error.html")



