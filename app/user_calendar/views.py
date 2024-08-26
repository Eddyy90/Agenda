from django.shortcuts import render

def Calendar(request):
    return render(request, "user_calendar/calendar.html", {
        'title' : 'calendar',
    })
