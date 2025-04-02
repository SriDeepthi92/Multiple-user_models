from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from materials.models import Material, compound
from .models import *
from .forms import *
# Create your views here.


class MaterialsListView(ListView):
    model = Material


    def get(self, request, *args, **kwargs):
            objects = Material.objects.all()
            context = {"materials": objects}
            return render(request, "Materials-list.html", context)

class CompListView(ListView):
    model = compound
    queryset = compound.objects.all()

    def get(self, request, *args, **kwargs):
        objects = compound.objects.all()
        context = {"object_list": objects}
        return render(request, "compound-list.html", context)
       
def createcompound(request):
        form = compoundForm()
        if request.method == 'POST':
    		#print('Printing POST:', request.POST)
            form = compoundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {'form': form}
        return render(request, 'add-compound.html', context)