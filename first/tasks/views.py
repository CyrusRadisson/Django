from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
# I have problem with the def index, because I need to show empty task list after each log in, but I don't know what to do.
def index(request):
    tasks = request.session.get("tasks",[])
    request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
                            

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "forms": form
            })
    
    return render(request, "tasks/add.html", {
        "forms": NewTaskForm()
    })
