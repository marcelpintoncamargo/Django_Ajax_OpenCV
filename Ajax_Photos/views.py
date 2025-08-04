from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from .forms import PhotoForm


def index_function(request):
    return render(request, 'index.html')
    # return HttpResponseRedirect("photo_add_path")


def photo_add_function(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    data = {}
    if request.accepts("application/json"):  ## This information came from main.js -->  ajax POST
        if form.is_valid():  ## This information came from forms.py
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {
        'form': form,
    }
    return render(request, 'Ajax_Photos/Ajax_Form_Images.html', context)
