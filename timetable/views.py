from django.shortcuts import render

def timetable(req):
    return render(req, "timetable.html")

def notes(req):
    return render(req, "notes.html")
