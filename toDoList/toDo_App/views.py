from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import UpdateView, DeleteView

# Create your views here.
def home(request):
    notes = Notes.objects.order_by("priority")
    return render(request, 'toDo_App/home.html', {"notes": notes})

class Update(UpdateView):
    model = Notes
    template_name = 'toDo_App/create.html'
    form_class = NotesForm

class Delete(DeleteView):
    model = Notes
    success_url = '/home/'
    template_name = 'toDo_App/delete.html'

def create(request):
    error = ''
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ошибка заполнения'

    form = NotesForm()

    data = {
        "form": form,
        "error": error
    }

    return render(request, 'toDo_App/create.html', data)
