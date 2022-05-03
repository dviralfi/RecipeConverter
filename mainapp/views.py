import re
from django.shortcuts import render

from mainapp.forms import FileAndNumForm
import RecipeConverterGenerator

def home(request):
    form = FileAndNumForm()
    context = {
    'form':form,
    'new_file_path':'',
    }

    if request.method == 'GET':
        return render(request, 'home.html', context)

    if request.method == 'POST':

        form = FileAndNumForm(request.POST,request.FILES)
        
        if form.is_valid():

            file = request.FILES['file']
            number = form.cleaned_data["number"]

            print(file, number)
            new_file_path = RecipeConverterGenerator.handle_file(file,number)

            context['new_file_path'] = new_file_path

            return render(request,'home.html',context)
        else:
            print("Form Not Valid... ")
            return render(request, 'home.html', context)

   

def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request,"contact.html", {})

