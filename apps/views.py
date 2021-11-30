from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView

from apps.resources import PersonResource
from .models import Person
from tablib import Dataset
from django.contrib import messages
from django.http import HttpResponse



def upload_file(request):
    if request.method == "POST":
        resource = PersonResource()
        dataset = Dataset()
        new_resource = request.FILES['excelFile']
        print(new_resource)
        if not new_resource.name.endswith('xlsx'):
            messages.error(request, 'only .xlsx file format is supported')
            return HttpResponseRedirect('/')
        else:
            get_data = dataset.load(new_resource.read(), format='xlsx')
            row = 0
            for data in get_data:
                try:
                    person = Person(
                        name = data[0],
                        email = data[1],
                        contact = data[2]
                    )
                    person.save()
                    row+=1
                except:pass

            messages.success(request, f'successfully upload {row} rows')

    return HttpResponseRedirect('/')


class HomeView(TemplateView):
    template_name = 'home.html'