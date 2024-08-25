from django.shortcuts import render


def dashboard(request):
    return render(request, "misc/Dashboard.html", {
        'title' : 'Dashboard',
    })