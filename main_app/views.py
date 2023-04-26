from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hedgehog, Toy
from .forms import FeedingForm


# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')


def hedgehogs_index(request):
  hedgehogs = Hedgehog.objects.all()
  return render(request, 'hedgehogs/index.html', {'hedgehogs': hedgehogs })

def hedgehogs_detail(request, hedgehog_id):
  hedgehog = Hedgehog.objects.get(id=hedgehog_id)
  toys_hedgehog_doesnt_have = Toy.objects.exclude(id__in = hedgehog.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'hedgehogs/detail.html', { 'hedgehog': hedgehog, 'feeding_form':feeding_form, 'toys': toys_hedgehog_doesnt_have })

def add_feeding(request, hedgehog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.hedgehog_id = hedgehog_id
    new_feeding.save()
  return redirect('detail', hedgehog_id=hedgehog_id)

def assoc_toy(request, hedgehog_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Hedgehog.objects.get(id=hedgehog_id).toys.add(toy_id)
  return redirect('detail', hedgehog_id=hedgehog_id)


class HedgehogCreate(CreateView):
  model = Hedgehog
  fields = ('name', 'breed', 'description', 'age')

class HedgehogUpdate(UpdateView):
  model = Hedgehog
  fields = ['breed', 'description', 'age']

class HedgehogDelete(DeleteView):
  model = Hedgehog
  success_url = '/hedgehogs/'

# <---- Toys Classes ---->

class ToysIndex(ListView):
  model = Toy

class ToysDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = '__all__'

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'