from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from mptt_hierarchy.forms import FileAddForm
from mptt_hierarchy.models import File


def home_view(request):
    return render(request, 'home.html', {'files': File.objects.all()})


def file_add_view(request):
    html = 'addfile.html'
    form = None

    if request.method == 'POST':
        form = FileAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(name=data['name'], parent=data['parent'])

        return HttpResponseRedirect(reverse('home'))

    else:
        form = FileAddForm()

    return render(request, html, {'form': form})
