from django.shortcuts import render

def timetable(req):
    return render(req, "timetable.html")
